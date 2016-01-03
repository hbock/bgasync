import unittest
from bgasync import api

class ApiBaseTests(unittest.TestCase):
    """ Tests for non-auto-generated API code and utilities. """
    def test_get_error_code_string(self):
        self.assertEqual("Device in wrong state to receive command", api.get_error_code_string(0x181))

    def test_get_error_code_string_unknown(self):
        self.assertEqual("Unknown error (0x5643)", api.get_error_code_string(0x5643))

    def test_get_address_string(self):
        self.assertEqual("aa:bb:cc:dd:ee:ff", api.get_address_string("\xaa\xbb\xcc\xdd\xee\xff"))
        self.assertEqual("aabbccddeeff", api.get_address_string("\xaa\xbb\xcc\xdd\xee\xff", delimiter=""))
        self.assertEqual("aa.bb.cc.dd.ee.ff", api.get_address_string("\xaa\xbb\xcc\xdd\xee\xff", delimiter="."))
