"""
Test utility to gather information on the device supporting BGAPI
(version information, flash, etc)
"""
import sys
import argparse
import binascii

from bgasync.api import *
from bgasync.twisted.protocol import BluegigaProtocol

from twisted.internet.serialport import SerialPort
from twisted.internet.defer import inlineCallbacks
from twisted.internet import reactor
from twisted.python import log

@inlineCallbacks
def command_response_cb(response, protocol):
    print("System information:\n  * Software version {}.{}.{} build {}\n  * Hardware version {}".format(
        response.major, response.minor, response.patch, response.build, response.hw
    ))
    print("  * LL version {}".format(response.ll_version))

    response = yield protocol.send_command(command_system_address_get())
    print("Bluetooth address: {}".format(
        ":".join(("%02x" % (ord(octet),) for octet in response.address))
    ))

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
    def handle_event_connection_status(self, event):
        print("Connection status (#{}):".format(event.connection))
        print("   Flags: {:02x}".format(event.flags))

    def handle_event_flash_ps_key(self, event):
        # 0xFFFF indicates last value
        if event.value != 0xFFFF:
            print("Flash PS key {}:".format(event.key))
            print("  Value = {}".format(binascii.hexlify(event.value)))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("serial_port", help="Serial/COM port connected to the Bluegiga device.")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    protocol = TestProtocol()
    port = SerialPort(protocol, args.serial_port, reactor, baudrate=256000)
    d = protocol.send_command(command_system_get_info())
    d.addCallback(command_response_cb, protocol)

    if args.verbose:
        log.startLogging(sys.stderr, setStdout=False)

    reactor.run()

if __name__ == "__main__":
    main()