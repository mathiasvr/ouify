#!/usr/bin/env python3

"""
Annotate MAC addresses with vendor names,
similar to Wireshark captures, based on OUI/IAB data.
"""
import sys
import argparse
from manuf import manuf # pip3 install git+https://github.com/coolbho3k/manuf

def insertSeparators(mac):
    return ':'.join(mac[i:i+2] for i in range(0, len(mac), 2))

# command line arguments
parser = argparse.ArgumentParser(description='Annotate MAC addresses with vendor names.')
parser.add_argument('-f', '--full', action='store_true', help='print whole MAC address instead of suffix')
parser.add_argument('-u', '--update', action='store_true', help='update Wireshark OUI definition file')
args = parser.parse_args()

try:
    parser = manuf.MacParser(manuf_name='ws_oui.txt', update=args.update)
    if args.update:
        print("OUI definitions updated.")
        exit(0)
except FileNotFoundError:
    print('Error: OUI definition file not found.\nRun "ouify.py -u" to download it.')
    exit(1)

for line in sys.stdin:
    line = line.strip()
    try:
        mac = parser._strip_mac(line).lower()
        if len(mac) != 12:
            raise ValueError()

        shortName = parser.get_all(line).manuf

        if shortName:
            print(shortName + "_" + insertSeparators(mac if args.full else mac[6:12]))
        else:
            print(insertSeparators(mac))

    except ValueError as err:
        print('Could not parse MAC: ' + line)
