#!/usr/bin/env python3
# coding: utf-8
#
# Version 2018.10.17
#

import os
import re
import sys


def usage():
    return '''

    Usage: oui <mac address>

    The MAC address can be in most any format of either 6 or 12 digits.
    Eg. aabb.ccdd.eeff, aa:bb:cc:dd:ee:ff, aa:bb:cc, aabb.c, etc.

    '''


def clean(unclean):
    # Replace non-word chars.
    return re.sub(r'\W+', '', unclean)


def get_oui_prefix(input):
    return f"{input[:2]}:{input[2:4]}:{input[4:6]}".upper()


def get_mac_vendor(prefix):
    wireshark_oui_file_path = ("/Applications/Wireshark.app/Contents"
                               "/Resources/share/wireshark/manuf"
                               )

    if not os.path.exists(wireshark_oui_file_path):
        print("I cannot find a Wireshark \"manuf\" file!")

    with open(wireshark_oui_file_path, 'r') as f:
        for line in f.readlines():
            # This is crap and should be case-insensitive.
            if line.startswith(prefix):
                return line.rstrip()

    return f"Result not found for: {prefix}"


def main():

    if len(sys.argv) != 2:
        print(usage())
        sys.exit(1)

    unclean_addr = sys.argv[1]

    print("{}".format(
        get_mac_vendor(
            get_oui_prefix(
                clean(unclean_addr)
            )
        )
      )
    )


if __name__ == "__main__":
    main()
