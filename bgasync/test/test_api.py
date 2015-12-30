import unittest
from bgasync import api

class ApiTest(unittest.TestCase):
    """
    Test examples of generated code from api.api
    """
    def setUp(self):
        pass

    def test_attclient_read_by_type_encode(self):
        cmd = api.command_attclient_read_by_type(
            connection=2,
            start=0x5643,
            end=0xbeef,
            uuid=b"\xef\xbe"
        )

        self.assertEqual(b'\x00\x08\x04\x02\x02\x43\x56\xef\xbe\x02\xef\xbe',
                         api.encode_command(cmd))

    def test_attclient_read_by_type_decode_response(self):
        # Test response with multiple parameters
        resp = api.response_attclient_read_by_type.decode(b"\x01\xef\xbe")
        self.assertEqual(1, resp.connection)
        self.assertEqual(0xBEEF, resp.result)

    def test_hardware_spi_transfer(self):
        cmd = api.command_hardware_spi_transfer(
            channel=5,
            data=b"foo"
        )
        self.assertEqual(b"\x00\x05\x07\x09\x05\x03foo", api.encode_command(cmd))

    def test_hardware_i2c_read(self):
        cmd = api.command_hardware_i2c_read(
            address=66,
            stop=0,
            length=5
        )
        self.assertEqual(b"\x00\x03\x07\x0A\x42\x00\x05", api.encode_command(cmd))

    def test_hardware_spi_transfer_decode_response(self):
        # Test decoding a response ending in uint8array
        resp = api.response_hardware_spi_transfer.decode(b"\xa5\x5a\x05\x04beef")
        self.assertEqual(0x5aa5, resp.result)
        self.assertEqual(0x05, resp.channel)
        self.assertEqual(b"beef", resp.data)

    def test_event_system_boot_decode(self):
        resp = api.event_system_boot.decode(b'\x43\x56\x01\x01\x00\x01\x02\x02\x00\x05\xFE\xEF')
        self.assertEqual(0x5643, resp.major)
        self.assertEqual(0x0101, resp.minor)
        self.assertEqual(0x0100, resp.patch)
        self.assertEqual(0x0202, resp.build)
        self.assertEqual(0x0500, resp.ll_version)
        self.assertEqual(0xFE, resp.protocol_version)
        self.assertEqual(0xEF, resp.hw)
