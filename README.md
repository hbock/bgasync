# `bgasync` - Asynchronous Bluegiga/BGAPI support for Python 3

`bgasync` is a Python library for communicating with Bluegiga products
supporting the BGAPI protocol (BLE112, BLED112, etc.).  The library
is focused on support for popular asynchronous I/O frameworks, including
`Twisted` and `asyncio`.

Development is currently in a very early state; the API may change drastically
without warning, and you will find bugs aplenty.  Once it gets into a more stable
state, I'm happy to accept issues, patches, pull requests, and feature requests.

If you're looking for a synchronous implementation in Python, there are several
other interesting repositories on Github.

## License

`bgasync` is licensed under the 2-clause ("Simplified") BSD license.
See the COPYING file.

## Python Support

Currently only 2.7 and Python 3.4+ are explicitly supported.

## Twisted Support

Twisted support for the BGAPI protocol is provided via the `bgasync.twisted` package.
Currently support is limited to working with commands and events in the BGAPI; the plan
is to provide higher-level APIs as well.

Twisted support for Windows on Python 3.5 is limited to sockets via select(); thus
the serial port support doesn't work yet.  Workarounds are forthcoming; for now you
can create a serial-TCP bridge in a separate process or thread and use BluegigaProtocol
on a TCP connection.

## `asyncio` support

`asyncio` support is currently planned but not developed.