import unittest
from bgasync import api

class ApiBaseTests(unittest.TestCase):
    """ Tests for non-auto-generated API code and utilities. """
    def test_get_error_code_string(self):
        self.assertEqual("Device in wrong state to receive command", api.get_error_code_string(0x181))

    def test_get_error_code_string_unknown(self):
        self.assertEqual("Unknown error (0x5643)", api.get_error_code_string(0x5643))

    def test_get_address_string(self):
        self.assertEqual("ff:ee:dd:cc:bb:aa", api.get_address_string_from_bytes("\xaa\xbb\xcc\xdd\xee\xff"))
        self.assertEqual("ffeeddccbbaa", api.get_address_string_from_bytes("\xaa\xbb\xcc\xdd\xee\xff", delimiter=""))
        self.assertEqual("ff.ee.dd.cc.bb.aa", api.get_address_string_from_bytes("\xaa\xbb\xcc\xdd\xee\xff", delimiter="."))

    def test_get_address_bytes_from_string(self):
        self.assertEqual(b"\xff\xee\xdd\xcc\xbb\xaa", api.get_address_bytes_from_string("aa:bb:cc:dd:ee:ff"))
        self.assertEqual(b"\xff\xee\xdd\xcc\xbb\xaa", api.get_address_bytes_from_string("aabbccddeeff"))
        self.assertEqual(b"\xff\xee\xdd\xcc\xbb\xaa", api.get_address_bytes_from_string("AA:BB:CC:dd:ee:ff"))

    def test_get_address_bytes_from_string_valueerror(self):
        # Odd length of characters
        self.assertRaises(ValueError, api.get_address_bytes_from_string, "foo")
        # Invalid digits
        self.assertRaises(ValueError, api.get_address_bytes_from_string, "fooo")
        # Too short
        self.assertRaises(ValueError, api.get_address_bytes_from_string, "aabbccddee")
        # Too long
        self.assertRaises(ValueError, api.get_address_bytes_from_string, "aabbccddeeffaa")
        # Empty
        self.assertRaises(ValueError, api.get_address_bytes_from_string, "")
