"""
Common functionality for implementing BGAPI.

NOTE: This file is not auto-generated.
"""

# BGAPI base types, constants, and data.
from struct import Struct
from collections import namedtuple

# BGAPI message types.
BGAPI_MESSAGE_TYPE_COMMAND = 0x00
BGAPI_MESSAGE_TYPE_EVENT   = 0x80

# Masks for 1st byte of BGAPI frame
BGAPI_MESSAGE_TYPE_MASK            = 0x80
BGAPI_MESSAGE_TECHNOLOGY_TYPE_MASK = 0x71
BGAPI_MESSAGE_LENGTH_HIGH_MASK     = 0x07

# BGAPI technology types
BGAPI_TECHNOLOGY_BLUETOOTH_SMART = 0
BGAPI_TECHNOLOGY_WIFI = 1

## Error codes

# BGAPI protocol errors
ERR_BGAPI_INVALID_PARAMETER     = 0x0180
ERR_BGAPI_DEVICE_IN_WRONG_STATE = 0x0181
ERR_BGAPI_OUT_OF_MEMORY         = 0x0182

ERR_CODE_STRING_MAP = {
    ERR_BGAPI_INVALID_PARAMETER:     "Invalid parameter",
    ERR_BGAPI_DEVICE_IN_WRONG_STATE: "Device in wrong state to receive command",
    ERR_BGAPI_OUT_OF_MEMORY:         "Out of memory"
}

def get_error_code_string(errorcode):
    """
    Translate a BGAPI error code into a human-readable string.

    Does not throw an exception on an unknown `errorcode`; simply returns
    "Unknown error (0xYYYY)".

    :param errorcode: BGAPI error code (16 bits)
    :return: A string corresponding to `errorcode`.
    """
    return ERR_CODE_STRING_MAP.get(errorcode, "Unknown error (0x{:04x})".format(errorcode))

def get_address_string(address_raw, delimiter=":"):
    """
    Convert a Bluetooth address in bytes form into a delimited string representation.

    :param address_raw: Bluetooth address, as a bytes instance.
    :param delimiter: Delimiter to use between octets.
    :return: A string representing `address_raw` delimited by `delimiter`.
    """
    return delimiter.join("{:02x}".format(ord(octet)) for octet in address_raw)

class Decodable(object):
    decoded_type = namedtuple('undefined', ())
    #: structure definition for decoded_type
    decode_struct = Struct("")
    #: True if this value ends with a uint8array
    ends_with_uint8array = False

    @classmethod
    def decode(cls, buffer):
        """
        Attempt to decode buffer (bytes) into a value of decoded_type.
        """
        if cls.ends_with_uint8array:
            # This is a godawful mess.  If we end the command/event with
            # a uint8array, we need to pull off the struct-packed part
            # from the array payload.
            buffer, array = buffer[:cls.decode_struct.size], buffer[cls.decode_struct.size:]
            unpacked_buffer = cls.decode_struct.unpack(buffer)
            array_size = unpacked_buffer[-1]
            assert array_size == len(array)
            c = (unpacked_buffer[:-1] + (array,))

        else:
            c = cls.decode_struct.unpack(buffer)

        # Build the decoded namedtuple
        return cls.decoded_type._make(c)

#: Structure definition for BGAPI message header
HEADER_STRUCT = Struct("<BBBB")

# BGAPI header:
#  [0] => Message Type, Technology Type, Length High
#  [1] => Length Low
#  [2] => Command class ID
#  [3] => Command ID

def encode_command(command):
    if command._ends_with_uint8array:
        assert isinstance(command[-1], (bytes, bytearray))
        # This is a slightly less godawful mess; only pack the first (n-1)
        # elements of the tuple and the length of the final array.
        # Append the final array to the payload
        c = command[:-1] + (len(command[-1]),)
        payload = command._struct.pack(*c) + command[-1]

    else:
        payload = command._struct.pack(*command)

    tech_id, class_id, command_id = command._id
    payload_len = len(payload)
    assert(payload_len < 2048)

    b0 = BGAPI_MESSAGE_TYPE_COMMAND | (tech_id << 3) | (payload_len >> 8)
    header = HEADER_STRUCT.pack(b0, (payload_len & 0xFF), class_id, command_id)

    return header + payload
