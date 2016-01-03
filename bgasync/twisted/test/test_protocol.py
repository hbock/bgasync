from twisted.trial import unittest

from bgasync import api
from bgasync.twisted import protocol
from twisted.test.proto_helpers import StringTransport

class BGMessageSpy(protocol.BluegigaProtocol):
    def __init__(self):
        protocol.BluegigaProtocol.__init__(self)
        self.cmd_resp_list = []
        self.event_list = []

    def process_command_response_raw(self, command_id, response_payload):
        self.cmd_resp_list.append((command_id, response_payload))

    def process_event_raw(self, event_id, event_payload):
        self.event_list.append((event_id, event_payload))

class ProtocolBaseTests(unittest.TestCase):
    """ Simple tests for validating Twisted BGAPI message sender/receiver base functionality """
    def setUp(self):
        self.proto = BGMessageSpy()

    def assert_nothing_received(self):
        self.assertEqual([], self.proto.cmd_resp_list)
        self.assertEqual([], self.proto.event_list)

    def test_spy(self):
        # Sanity check
        self.assert_nothing_received()

    def test_decode_full_event(self):
        self.proto.dataReceived(b"\x80\x04\x0A\x0B5643")
        self.assertEqual(((0x0A, 0x0B), b'5643'), self.proto.event_list[0])
        self.assertEqual([], self.proto.cmd_resp_list)

    def test_decode_multiple_events(self):
        """ Test receiving multiple events in one dataReceived call """
        self.proto.dataReceived(b"\x80\x04\x0A\x0B5643\x80\x04\x0A\x0BYEAH\x80\x04\x0A\x0BRITE")
        self.assertEqual(3, len(self.proto.event_list))
        self.assertEqual(((0x0A, 0x0B), b'5643'), self.proto.event_list[0])
        self.assertEqual(((0x0A, 0x0B), b'YEAH'), self.proto.event_list[1])
        self.assertEqual(((0x0A, 0x0B), b'RITE'), self.proto.event_list[2])
        self.assertEqual([], self.proto.cmd_resp_list)

    def test_decode_multiple_events_split(self):
        """ Test receiving multiple events split across multiple dataReceived calls """
        self.proto.dataReceived(b"\x80\x08\x0A\x0B56")
        self.proto.dataReceived(b"43YEAH\x80\x08\x0A\x0BRIGHTNOW")
        self.assertEqual(2, len(self.proto.event_list))
        self.assertEqual(((0x0A, 0x0B), b'5643YEAH'), self.proto.event_list[0])
        self.assertEqual(((0x0A, 0x0B), b'RIGHTNOW'), self.proto.event_list[1])
        self.assertEqual([], self.proto.cmd_resp_list)

    def test_decode_full_cmd_resp(self):
        self.proto.dataReceived(b"\x00\x0A\x0B\x0CHabberdash")
        self.assertEqual([], self.proto.event_list)
        self.assertEqual(((0x0B, 0x0C), b'Habberdash'), self.proto.cmd_resp_list[0])

    def test_decode_partial_event(self):
        # Partial header
        self.proto.dataReceived(b"\x80\x04")
        self.assert_nothing_received()
        # Remaining header
        self.proto.dataReceived(b"\x0A\x0B")
        self.assert_nothing_received()
        # Partial payload
        self.proto.dataReceived(b"YE")
        self.assert_nothing_received()
        # Remaining payload
        self.proto.dataReceived(b"AH")
        self.assertEqual(((0x0A, 0x0B), b'YEAH'), self.proto.event_list[0])

    def test_decode_partial_cmd_resp(self):
        # Partial header
        self.proto.dataReceived(b"\x00\x04")
        self.assert_nothing_received()
        # Remaining header
        self.proto.dataReceived(b"\x0A\x0B")
        self.assert_nothing_received()
        # Partial payload
        self.proto.dataReceived(b"YE")
        self.assert_nothing_received()
        # Remaining payload
        self.proto.dataReceived(b"AH")
        self.assertEqual(((0x0A, 0x0B), b'YEAH'), self.proto.cmd_resp_list[0])
        self.assertEqual([], self.proto.event_list)

class ProtocolTests(unittest.TestCase):
    """ Tests for validating Twisted BGAPI message sender/receiver higher level functionality """
    def setUp(self):
        self.proto = protocol.BluegigaProtocol()
        self.proto.transport = StringTransport()

    # Test sending a command and decoding its responses from the real API
    def test_gap_connect_direct_response(self):
        cmd = api.command_gap_connect_direct(
            address=b"abcdef", addr_type=1,
            conn_interval_min=50, conn_interval_max=60,
            timeout=50, latency=50
        )

        def foo(response):
            self.assertEqual(0xBEEF, response.result)
            self.assertEqual(0x01, response.connection_handle)

        d = self.proto.send_command(cmd)
        d.addCallback(foo)
        self.assertEqual(b"\x00\x0f\x06\x03abcdef\x012\x00<\x002\x002\x00", self.proto.transport.value())

        # command = GAP (0x06) Connect Direct (0x03)
        # resp = result=0xBEEF; handle=0x01
        self.proto.dataReceived(b"\x00\x03\x06\x03\xEF\xBE\x01")
        return d

    def test_sm_delete_bonding_response(self):
        cmd = api.command_sm_delete_bonding(handle=0xAA)

        def foo(response):
            self.assertEqual(0xFEED, response.result)

        d = self.proto.send_command(cmd)
        d.addCallback(foo)

        # command = SM (0x05) Delete Bonding (0x02)
        self.assertEqual(b"\x00\x01\x05\x02\xaa", self.proto.transport.value())
        # resp = errorcode=0xFEED
        self.proto.dataReceived(b"\x00\x02\x05\x02\xED\xFE")

        return d

    def test_multiple_commands(self):
        cd_cmd = api.command_gap_connect_direct(
            address=b"abcdef", addr_type=1,
            conn_interval_min=50, conn_interval_max=60,
            timeout=50, latency=50
        )
        db_cmd = api.command_sm_delete_bonding(handle=0xAA)

        def db_callback(response):
            self.assertEqual(0xFEED, response.result)

        def cd_callback(response):
            pass

        db_deferred = self.proto.send_command(db_cmd)
        db_deferred.addCallback(db_callback)

        cd_deferred = self.proto.send_command(cd_cmd)
        cd_deferred.addCallback(cd_callback)

        # command = SM (0x05) Delete Bonding (0x02)
        self.assertEqual(b"\x00\x01\x05\x02\xaa", self.proto.transport.value())

        # Clear transport
        self.proto.transport.clear()

        # command = SM (0x05) Delete Bonding (0x02)
        # resp = errorcode=0xFEED
        self.proto.dataReceived(b"\x00\x02\x05\x02\xED\xFE")
        self.assertTrue(db_deferred.called)

        # Second (queed) command should now be sent
        self.assertEqual(b"\x00\x0f\x06\x03abcdef\x012\x00<\x002\x002\x00", self.proto.transport.value())
        self.proto.transport.clear()

        # command = GAP (0x06) Connect Direct (0x03)
        # resp = result=0xBEEF; handle=0x01
        self.proto.dataReceived(b"\x00\x03\x06\x03\xEF\xBE\x01")

        # No more commands to send
        self.assertEqual(b"", self.proto.transport.value())

        return cd_deferred

    def test_event_decode_and_dispatch(self):
        event_list = []

        class EventCaptureProtocol(protocol.BluegigaProtocol):
            def handle_event_connection_disconnected(self, event):
                event_list.append(event)

        proto = EventCaptureProtocol()
        proto.transport = StringTransport()

        proto.dataReceived(b"\x80\x03\x03\x04\x05\xEF\xBE")
        self.assertEqual(1, len(event_list))
        self.assertEqual(5, event_list[0].connection)
        self.assertEqual(0xBEEF, event_list[0].reason)
