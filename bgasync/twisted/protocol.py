"""
bgasync.twisted.protocol - Main transmit/receive protocol for Twisted.
"""
from twisted.internet.protocol import Protocol
from bgasync.apibase import *
from bgasync import api

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
    def __init__(self):
        #: Buffered data (bytes)
        self.buffer = b""
        self.state = STATE_RECV_HEADER

        # Current message data; only valid in STATE_RECV_PAYLOAD
        self.current_message_length = 0
        self.current_message_id = None
        self.current_message_type = None

    def process_header(self):
        header, self.buffer = self.buffer[:HEADER_LENGTH], self.buffer[HEADER_LENGTH:]

        b0, msg_ll, class_id, command_id = HEADER_STRUCT.unpack(header)
        msg_type = b0 & BGAPI_MESSAGE_TYPE_MASK
        msg_tt   = (b0 & BGAPI_MESSAGE_TECHNOLOGY_TYPE_MASK) >> 4
        msg_lh   = (b0 & BGAPI_MESSAGE_LENGTH_HIGH_MASK)

        self.current_message_length = (msg_lh << 8) | msg_ll
        self.current_message_id = (class_id, command_id)
        self.current_message_type = msg_type

        # TODO: process different/unknown technology types

        self.state = STATE_RECV_PAYLOAD

    def process_payload(self):
        payload, self.buffer = self.buffer[:self.current_message_length], \
                               self.buffer[self.current_message_length:]

        if BGAPI_MESSAGE_TYPE_EVENT == self.current_message_type:
            self.process_event(self.current_message_id, payload)

        elif BGAPI_MESSAGE_TYPE_COMMAND == self.current_message_type:
            self.process_command_response(self.current_message_id, payload)

        self.state = STATE_RECV_HEADER

    def process_event(self, event, event_payload):
        """
        Process event (class_id, event_id) with event_payload.
        """
        raise NotImplementedError()

    def process_command_response(self, command_id, response_payload):
        raise NotImplementedError()

    def dataReceived(self, data):
        self.buffer += data

        if STATE_RECV_HEADER == self.state:
            if len(self.buffer) >= HEADER_LENGTH:
                self.process_header()

        if STATE_RECV_PAYLOAD == self.state:
            if len(self.buffer) >= self.current_message_length:
                self.process_payload()

class BluegigaProtocol(BluegigaProtocolBase):
    def send_command(self, command):
        self.transport.write(api.encode_command(command))

    def process_event(self, event_id, event_payload):
        try:
            event = api.EVENT_TYPE_MAP[event_id]
            # TODO: decode me

        except KeyError:
            print("Unknown class/event combination {}".format(event_id))

    def process_command_response(self, command_id, response_payload):
        try:
            return_type = api.COMMAND_RETURN_TYPE_MAP[command_id]
            command = return_type.decode(response_payload)
            print(repr(command))

        except KeyError:
            print("Unknown command {}".format(command_id))
