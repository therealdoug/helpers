#!/usr/bin/python

'''
This script will convert between different MAC address formats (4-Dot, standard)
To do this bash:  sed 's/\://g;s/.\{4\}/&./g;s/\.$//g' 00:50:56:9A:7A:5D
Example:
  00:50:56:9A:7A:5D > 0050.569A.7A5D
  0050.334A.773F > 00:50:33:4A:77:3F
'''

import sys
import re
import string


# Normalize input.  Resultant string should be 12 char


def normalize(mac):
    mac = re.sub('[\.\:]', '', mac)
    return mac


if ":" in sys.argv[1]:
    _str = re.sub(r"(.{4})", r"\1.", normalize(sys.argv[1]))
    print _str.rstrip(".")
else:
    _str = re.sub(r"(.{2})", r"\1:", normalize(sys.argv[1]))
    print _str.rstrip(":")
