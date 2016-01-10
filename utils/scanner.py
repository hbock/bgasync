"""
Test utility to create a Bluetooth LE scan table.
"""
import sys
import argparse

from bgasync import api
from bgasync.twisted.protocol import BluegigaProtocol

from twisted.internet.serialport import SerialPort
from twisted.internet.defer import inlineCallbacks
from twisted.internet.task import deferLater
from twisted.internet import reactor
from twisted.python import log

class ScannerProtocol(BluegigaProtocol):
    def handle_event_gap_scan_response(self, event):
        print("Received advertising event [sender={}]: {}".format(api.get_address_string_from_bytes(event.sender), event))

@inlineCallbacks
def stop_discovery(protocol):
    print("Stopping discovery.")
    response = yield protocol.send_command(api.command_gap_end_procedure())
    if response.result != 0:
        print("Error stopping discovery! {}".format(api.get_error_code_string(response.result)))

    # End program
    reactor.stop()

@inlineCallbacks
def command_response_cb(response, protocol, duration):
    if response.result != 0:
        print("Error setting scan parameters: {}".format(api.get_error_code_string(response.result)))

    response = yield protocol.send_command(api.command_gap_discover(mode=api.gap_discover_mode.discover_observation.value))
    if response.result != 0:
        print("Error starting discovery! {}".format(api.get_error_code_string(response.result)))

        # If we're in the wrong state, we may have simply exited
        # while still discovering.
        # Try to fix it by ending the GAP procedure and start over.
        if response.result == api.ERR_BGAPI_DEVICE_IN_WRONG_STATE:
            response = yield protocol.send_command(api.command_gap_end_procedure())

            # Need a Deferred delay, but no action.
            yield deferLater(reactor, 0.1, lambda: None)

            response = yield protocol.send_command(api.command_gap_discover(mode=api.gap_discover_mode.discover_observation.value))

        # Otherwise, we're unable to proceed.
        else:
            print("Terminating on error.")
            reactor.stop()

    else:
        print("Discovery started.")
        reactor.callLater(duration, stop_discovery, protocol)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("serial_port", help="Serial/COM port connected to the Bluegiga device.")
    parser.add_argument("-d", "--duration", type=int, help="Specify duration of device discovery", default=60)
    parser.add_argument("-v", "--verbose", action="store_true", help="Turn on verbose logging")
    args = parser.parse_args()

    print("Starting scanner (duration {} seconds)".format(args.duration))
    protocol = ScannerProtocol()
    port = SerialPort(protocol, args.serial_port, reactor, baudrate=256000)
    d = protocol.send_command(api.command_gap_set_scan_parameters(scan_interval=0x4B, scan_window=0x32, active=1))
    d.addCallback(command_response_cb, protocol, args.duration)

    if args.verbose:
        log.startLogging(sys.stderr, setStdout=False)

    reactor.run()

if __name__ == "__main__":
    main()
