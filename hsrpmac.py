#!/usr/bin/python

'''
This helper script will take an integer input representing a VLAN ID and
output the HSRP vMAC for that VLAN.
'''

import sys

print "0000.OC9F.F" + "{0:X}".format(int(sys.argv[1])).zfill(3)
