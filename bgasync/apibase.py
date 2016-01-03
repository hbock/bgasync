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
ERR_BGAPI_INVALID_PARAMETER       = 0x0180
ERR_BGAPI_DEVICE_IN_WRONG_STATE   = 0x0181
ERR_BGAPI_OUT_OF_MEMORY           = 0x0182
ERR_BGAPI_FEATURE_NOT_IMPLEMENTED = 0x0183
ERR_BGAPI_COMMAND_NOT_RECOGNIZED  = 0x0184
ERR_BGAPI_TIMEOUT                 = 0x0185
ERR_BGAPI_NOT_CONNECTED           = 0x0186
ERR_BGAPI_UNDERFLOW_OR_OVERFLOW   = 0x0187
ERR_BGAPI_USER_ATTRIBUTE          = 0x0188
ERR_BGAPI_INVALID_LICENSE_KEY     = 0x0189
ERR_BGAPI_COMMAND_TOO_LONG        = 0x018A
ERR_BGAPI_OUT_OF_BONDS            = 0x018B

# Bluetooth errors
ERR_BT_AUTHENTICATION_FAILURE     = 0x0205
ERR_BT_PIN_OR_KEY_MISSING         = 0x0206
ERR_BT_MEMORY_CAPACITY_EXCEEDED   = 0x0207
ERR_BT_CONNECTION_TIMEOUT         = 0x0208
ERR_BT_CONNECTION_LIMIT_EXCEEDED  = 0x0209
ERR_BT_COMMAND_DISALLOWED         = 0x020C
ERR_BT_INVALID_PARAMETERS         = 0x0212
ERR_BT_REMOTE_USER_TERMINATED     = 0x0213
ERR_BT_LOCAL_USER_TERMINATED      = 0x0216
ERR_BT_LL_RESPONSE_TIMEOUT        = 0x0222
ERR_BT_LL_INSTANT_PASSED          = 0x0228
ERR_BT_CONTROLLER_BUSY            = 0x023A
ERR_BT_UNACCEPTABLE_CONN_INTERVAL = 0x023B
ERR_BT_DIRECTED_ADV_TIMEOUT       = 0x023C
ERR_BT_MIC_FAILURE                = 0x023D
ERR_BT_CONNECTION_ESTABLISH_FAIL  = 0x023E

# Security Manager errors
ERR_SM_PASSKEY_ENTRY_FAILED        = 0x0301
ERR_SM_OOB_DATA_NOT_AVAILABLE      = 0x0302
ERR_SM_AUTHENTICATION_REQUIREMENTS = 0x0303
ERR_SM_CONFIRM_VALUE_FAILED        = 0x0304
ERR_SM_PAIRING_NOT_SUPPORTED       = 0x0305
ERR_SM_ENCRYPTION_KEY_SIZE         = 0x0306
ERR_SM_COMMAND_NOT_SUPPORTED       = 0x0307
ERR_SM_UNSPECIFIED_REASON          = 0x0308
ERR_SM_REPEATED_ATTEMPTS           = 0x0309
ERR_SM_INVALID_PARAMETERS          = 0x030A

ERR_CODE_STRING_MAP = {
    # BGAPI
    ERR_BGAPI_INVALID_PARAMETER:       "BGAPI: invalid parameter",
    ERR_BGAPI_DEVICE_IN_WRONG_STATE:   "Device in wrong state to receive command",
    ERR_BGAPI_OUT_OF_MEMORY:           "Out of memory",
    ERR_BGAPI_FEATURE_NOT_IMPLEMENTED: "Feature not implemented",
    ERR_BGAPI_COMMAND_NOT_RECOGNIZED:  "Command not recognized",
    ERR_BGAPI_TIMEOUT:                 "Command or procedure failed due to timeout",
    ERR_BGAPI_NOT_CONNECTED:           "Connection handle is not valid [not connected]",
    ERR_BGAPI_UNDERFLOW_OR_OVERFLOW:   "Command would cause overflow or underflow error",
    ERR_BGAPI_USER_ATTRIBUTE:          "User attribute was accessed through API which is not supported",
    ERR_BGAPI_INVALID_LICENSE_KEY:     "No valid license key found",
    ERR_BGAPI_COMMAND_TOO_LONG:        "Command maximum length exceeded",
    ERR_BGAPI_OUT_OF_BONDS:            "Bonding procedure can't be started; no space for bond",

    # BT
    ERR_BT_AUTHENTICATION_FAILURE:     "Pairing or authentication failure; incorrect PIN or link key",
    ERR_BT_PIN_OR_KEY_MISSING:         "Pairing failed because of missing key",
    ERR_BT_MEMORY_CAPACITY_EXCEEDED:   "Controller is out of memory",
    ERR_BT_CONNECTION_TIMEOUT:         "Link supervision timeout exceeded",
    ERR_BT_CONNECTION_LIMIT_EXCEEDED:  "Controller is at connection limit",
    ERR_BT_COMMAND_DISALLOWED:         "Command requested cannot be executed in current controller state",
    ERR_BT_INVALID_PARAMETERS:         "Command contained invalid parameters",
    ERR_BT_REMOTE_USER_TERMINATED:     "User on the remote device terminated the connection",
    ERR_BT_LOCAL_USER_TERMINATED:      "Local device terminated the connection",
    ERR_BT_LL_RESPONSE_TIMEOUT:        "Connection terminated due to link-layer procedure timeout",
    ERR_BT_LL_INSTANT_PASSED:          "Received link-layer control packet where instant was in the past",
    ERR_BT_CONTROLLER_BUSY:            "Operation rejected because controller is busy",
    ERR_BT_UNACCEPTABLE_CONN_INTERVAL: "Remote device terminated the connection due to an unacceptable connection interval",
    ERR_BT_DIRECTED_ADV_TIMEOUT:       "Directed advertising completed without a connection being established",
    ERR_BT_MIC_FAILURE:                "Connection terminated due to failed MIC on received packet",
    ERR_BT_CONNECTION_ESTABLISH_FAIL:  "LL initiated connection; the controller did not receive any packets from the remote end",

    # SM
    ERR_SM_PASSKEY_ENTRY_FAILED:        "User input of passkey failed (possibly canceled)",
    ERR_SM_OOB_DATA_NOT_AVAILABLE:      "Out of band data is not available for authentication",
    ERR_SM_AUTHENTICATION_REQUIREMENTS: "Pairing authentication requirements cannot be met due to I/O capabilities of one or both devices",
    ERR_SM_CONFIRM_VALUE_FAILED:        "The confirm value does not match the calculated compare value",
    ERR_SM_PAIRING_NOT_SUPPORTED:       "Pairing is not supported by the device",
    ERR_SM_ENCRYPTION_KEY_SIZE:         "Encryption key size is insufficient for the security requirements of the device",
    ERR_SM_COMMAND_NOT_SUPPORTED:       "The SMP command received is not supported on this device",
    ERR_SM_UNSPECIFIED_REASON:          "Pairing failed due to an unspecified reason",
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
