"""
bgasync.twisted.protocol - Main transmit/receive protocol for Twisted.
"""
from twisted.internet.protocol import Protocol
from twisted.internet.defer import Deferred
from twisted.logger import Logger

from bgasync.apibase import *
from bgasync import api

from collections import deque

__all__ = [
    "BluegigaProtocolBase",
    "BluegigaProtocol"
]

(STATE_RECV_HEADER,
 STATE_RECV_PAYLOAD) = range(2)

HEADER_LENGTH = HEADER_STRUCT.size

class BluegigaProtocolBase(Protocol):
    """
    Base BGAPI message sender/receiver.
    """
    log = Logger()

    def __init__(self):
        #: Buffered data (bytes)
        self.buffer = b""
        self.state = STATE_RECV_HEADER

        # Current message data; only valid in STATE_RECV_PAYLOAD
        self.current_message_length = 0
        self.current_message_id = None
        self.current_message_type = None

        self.command_queue = deque()
        self.command_response_deferred_queue = deque()

    def process_header(self):
        header, self.buffer = self.buffer[:HEADER_LENGTH], self.buffer[HEADER_LENGTH:]

        b0, msg_ll, class_id, command_id = HEADER_STRUCT.unpack(header)
        msg_type = b0 & BGAPI_MESSAGE_TYPE_MASK
        msg_tt   = (b0 & BGAPI_MESSAGE_TECHNOLOGY_TYPE_MASK) >> 4
        msg_lh   = (b0 & BGAPI_MESSAGE_LENGTH_HIGH_MASK)

        self.current_message_length = (msg_lh << 8) | msg_ll
        self.current_message_id = (class_id, command_id)
        self.current_message_type = msg_type

        self.log.debug(
            "Received BGAPI header: type={type:02x}; length={length}; class={class_id} / command={command_id}",
            type=msg_type, length=self.current_message_length, class_id=class_id, command_id=command_id
        )
        # TODO: process different/unknown technology types

        self.state = STATE_RECV_PAYLOAD

    def process_payload(self):
        payload, self.buffer = self.buffer[:self.current_message_length], \
                               self.buffer[self.current_message_length:]

        if BGAPI_MESSAGE_TYPE_EVENT == self.current_message_type:
            self.log.debug("Received event {event}; payload raw = {raw!r}",
                           event=self.current_message_id, raw=payload)
            self.process_event(self.current_message_id, payload)

        elif BGAPI_MESSAGE_TYPE_COMMAND == self.current_message_type:
            self.log.debug("Received command response {event}; payload raw = {raw!r}",
                           event=self.current_message_id, raw=payload)
            self.process_command_response(self.current_message_id, payload)

        self.state = STATE_RECV_HEADER

    def process_event(self, event, event_payload):
        """
        Process a raw BGAPI event received on the wire.

        :param event: A tuple `(class_id, event_number)` uniquely identifying the event.
        :param response_payload: The raw payload of the event as a `bytes` object.
        """
        raise NotImplementedError()

    def process_command_response(self, command_id, response_payload):
        """
        Process a raw BGAPI command response received on the wire.

        :param command_id: A tuple `(class_id, command_number)` uniquely identifying the command.
        :param response_payload: The raw payload of the command as a `bytes` object.
        """
        try:
            return_type = api.COMMAND_RETURN_TYPE_MAP[command_id]
            command = return_type.decode(response_payload)

            # We expect that the response deferred queue cannot be empty;
            # i.e., we should not be receiving unsolicited command responses.
            assert self.command_response_deferred_queue

            deferred = self.command_response_deferred_queue.popleft()
            deferred.callback(command)

            # If commands are queued up, pop and consume one.
            if self.command_queue:
                command = self.command_queue.popleft()
                self._write_command(command)

        except KeyError:
            self.log.error("Received command response for unknown command {cmd}", cmd=command_id)

    def _write_command(self, command):
        """ Helper for writing a command out to the transport. """
        command_encoded = api.encode_command(command)
        self.log.debug("Transmitting command {cmd} [raw = {raw!r}]", cmd=command, raw=command_encoded)
        self.transport.write(command_encoded)


    def send_command(self, command):
        """
        Send a BGAPI command (from `bgasync.api`) to the target device.

        :param command: A BGAPI command instance.
        :return: A `Deferred` instance that will be called back with the
                 command response from the target device.

        Note that `command` may not be sent to the device immediately.  If multiple
        commands are in flight, only one is sent at a time until the last command's
        response has been received.
        """
        # We have no commands in flight, write to the transport immediately.
        # Otherwise, enqueue the command to be sent later; the API documentation
        # suggests not sending multiple commands to the device without first
        # receiving the response.
        if not self.command_response_deferred_queue:
            self._write_command(command)

        else:
            self.command_queue.append(command)

        # Store deferred for command response.
        deferred = Deferred()
        self.command_response_deferred_queue.append(deferred)

        return deferred

    def dataReceived(self, data):
        # TODO: faster buffering
        self.buffer += data

        if STATE_RECV_HEADER == self.state:
            if len(self.buffer) >= HEADER_LENGTH:
                self.process_header()

        if STATE_RECV_PAYLOAD == self.state:
            if len(self.buffer) >= self.current_message_length:
                self.process_payload()

class BluegigaProtocol(BluegigaProtocolBase):
    def process_event(self, event_id, event_payload):
        try:
            event_type = api.EVENT_TYPE_MAP[event_id]
            event = event_type.decode(event_payload)
            self.log.debug("Received API event: {event}", event=event)

        except KeyError:
            self.log.error("Received unknown event type {event}", event=event_id)
