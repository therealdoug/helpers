#!/usr/bin/python
# This scriplet will take an integer input and output the HSRP vMAC for that
# associated VLAN.

import sys

print "0000.OC9F.F" + "{0:X}".format(int(sys.argv[1])).zfill(3)
