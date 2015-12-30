import unittest

from bgasync.twisted import protocol


class BGMessageSpy(protocol.BluegigaProtocolBase):
    def __init__(self):
        super().__init__()
        self.cmd_resp_list = []
        self.event_list = []

    def process_command_response(self, command_id, response_payload):
        self.cmd_resp_list.append((command_id, response_payload))

    def process_event(self, event, event_payload):
        self.event_list.append((event, event_payload))

class ProtocolBaseTests(unittest.TestCase):
    """ Simple tests for validating Twisted BGAPI message sender/receiver """
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
    """ Simple tests for validating Twisted BGAPI message sender/receiver """
    def setUp(self):
        self.proto = protocol.BluegigaProtocol()

    # Test decoding a few select command responses from the real API
    def test_gap_connect_direct_response(self):
        # command = GAP (0x06) Connect Direct (0x03)
        # resp = result=0xBEEF; handle=0x01
        self.proto.dataReceived(b"\x00\x03\x06\x03\xEF\xBE\x01")
        # TODO deferred?

    def test_sm_delete_bonding_response(self):
        # command = SM (0x05) Delete Bonding (0x02)
        # resp = errorcode=0xFEED
        self.proto.dataReceived(b"\x00\x02\x05\x02\xED\xFE")
        # TODO deferred?
