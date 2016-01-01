from setuptools import setup
import sys

# Basic list of requirements
# TODO: I guess neither of these are REQUIRED, but strongly
# recommended.  At least, on 3.x, Twisted is not required,
# but not excluded either?
require_list = [
    "Twisted",
    "pyserial",
]

# Backport of enum module to 2.x and < 3.4
if sys.version < (3, 0):
    require_list.append("enum34")

setup(
    name="bgasync",
    version="0.1",
    description="Bluegiga BGAPI support for Twisted and asyncio",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: BSD",
        "Framework :: Twisted",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Communications",
        "Topic :: Software Development :: Libraries",
        "Operating System :: OS Independent"
    ],
    keywords="bluetooth ble bluegiga bgapi twisted asyncio",
    url="https://github.com/hbock/bgasync",
    author="Harry Bock",
    author_email="bock.harryw@gmail.com",
    license="BSD",
    packages=[
        "bgasync"
    ],
    install_requires=require_list,
    zip_safe=True
)