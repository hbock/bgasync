"""
Test utility to gather information on the device supporting BGAPI
(version information, flash, etc), and to perform various operations
(clear persistent store, bonding information, etc.)
"""
import sys
import argparse
import binascii

from bgasync.api import *
from bgasync.twisted.protocol import BluegigaProtocol

from twisted.internet.serialport import SerialPort
from twisted.internet.defer import inlineCallbacks
from twisted.internet.defer import Deferred
from twisted.internet import reactor
from twisted.python import log

def print_system_info(response):
    print("System information:\n  * Software version {}.{}.{} build {}\n  * Hardware version {}".format(
        response.major, response.minor, response.patch, response.build, response.hw
    ))
    print("  * LL version {}".format(response.ll_version))

@inlineCallbacks
def devinfo_response_cb(response, protocol):
    print_system_info(response)

    response = yield protocol.send_command(command_system_address_get())
    print("Bluetooth address: {}".format(get_address_string_from_bytes(response.address)))

    response = yield protocol.send_command(command_system_get_counters())
    print("Device counters:\n"
          "  * TX frames {} (retry {})\n"
          "  * RX frames {} (fail {})\n"
          "  * Buffer count: {}".format(
        response.txok, response.txretry,
        response.rxok, response.rxfail,
        response.mbuf
    ))

    # If system_get_connections() is sent before flash_ps_dump(), we don't
    # get the events for the PS dump.  Somehow we need to wait for expected
    # connection_status events?
    response = yield protocol.send_command(command_system_get_connections())
    print("Max supported connections: {}".format(response.maxconn))

    # flash_ps_dump() provides no useful response, so we ignore it.
    yield protocol.send_command(command_flash_ps_dump())

    # Wait 3 seconds, and terminate.
    reactor.callLater(3, reactor.stop)

class TestProtocol(BluegigaProtocol):
    def __init__(self):
        super(TestProtocol, self).__init__()
        self.system_boot_waiter_list = []

    def wait_for_system_boot(self):
        d = Deferred()
        self.system_boot_waiter_list.append(d)
        return d

    def handle_event_system_boot(self, event):
        for deferred in self.system_boot_waiter_list:
            deferred.callback(event)

    def handle_event_connection_status(self, event):
        print("Connection status (#{}):".format(event.connection))
        print("   Flags: {:02x}".format(event.flags))

    def handle_event_flash_ps_key(self, event):
        # 0xFFFF indicates last value
        if event.value != 0xFFFF:
            print("Flash PS key {}:".format(event.key))
            print("  Value = {}".format(binascii.hexlify(event.value)))

    def handle_event_sm_bond_status(self, event):
        print(event)

    def connectionLost(self, reason=None):
        # Serial port  went away
        print("Connection lost!")
        reactor.stop()

def bgtool_devinfo(protocol, args):
    """ Retrieve BLE(D) device information """
    d = protocol.send_command(command_system_get_info())
    d.addCallback(devinfo_response_cb, protocol)

def list_bonds_response_cb(response, protocol, args):
    print("Number of active bonds: {}".format(response.bonds))
    reactor.callLater(1, reactor.stop)

def delete_bonds_response_cb(response, protocol, args):
    print("  Result: {}".format(get_error_code_string(response.result)))
    reactor.stop()

def bgtool_bonds(protocol, args):
    """ Perform a system reset of the BGAPI device """
    if args.delete_all:
        print("Deleting all bonds.")

        d = protocol.send_command(command_sm_delete_bonding(handle=0xFF))
        d.addCallback(delete_bonds_response_cb, protocol, args)

    else:
        print("Listing bonded devices.")
        d = protocol.send_command(command_sm_get_bonds())
        d.addCallback(list_bonds_response_cb, protocol, args)

def bgtool_reset(protocol, args):
    """ Perform a system reset of the BGAPI device """
    dfu = 1 if args.dfu else 0
    d = protocol.send_command(command_system_reset(boot_in_dfu=dfu))
    # FIXME: reset doesn't get a response, and causes the BLED112 dongle
    # serial port to go away (expected).  Twisted calls connectionLost()
    # but there is still an exception on win32.

def bgtool_run(protocol, args):
    cmd = args.subparser_name
    cmd_vector = {
        "ps": None,
        "bonds": bgtool_bonds,
        "devinfo": bgtool_devinfo,
        "reset": bgtool_reset,
    }

    try:
        cmd_vector[cmd](protocol, args)

    except KeyError:
        sys.stderr.write("Unknown command: {}\n".format(cmd))
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser()

    # Positional
    parser.add_argument("serial_port", help="Serial/COM port connected to the Bluegiga device.")
    # Optional
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose log output")

    subparsers = parser.add_subparsers(dest='subparser_name', help='sub-command help')

    parser_devinfo = subparsers.add_parser('devinfo', help='Get device information')

    parser_bonds = subparsers.add_parser('bonds', help='Access bonds')
    parser_bonds.add_argument("--delete-all", action="store_true", help="Delete all bonds")

    parser_reset = subparsers.add_parser('reset', help='Reset device')
    parser_reset.add_argument("--dfu", action="store_true", help="Boot into Device Firmware Update (DFU) mode")


    args = parser.parse_args()

    protocol = TestProtocol()
    port = SerialPort(protocol, args.serial_port, reactor, baudrate=256000)

    bgtool_run(protocol, args)

    if args.verbose:
        log.startLogging(sys.stderr, setStdout=False)

    reactor.run()

if __name__ == "__main__":
    main()