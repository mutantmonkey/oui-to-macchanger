#!/usr/bin/python3
################################################################################
# oui_to_macchanger.py - convert official oui.txt to macchanger format
#
# author: mutantmonkey <mutantmonkey@mutantmonkey.in>
################################################################################

import re

__author__ = "mutantmonkey <mutantmonkey@mutantmonkey.in>"
__license__ = "WTFPL"

match = r'^([0-9A-F]{2})\-([0-9A-F]{2})\-([0-9A-F]{2})\s+\(hex\)\s+(.+)$'

with open('oui.txt', 'rb') as f:
    for line in f:
        try:
            line = line.decode('utf-8')
            m = re.match(match, line)
        except UnicodeDecodeError:
            m = None

        if m:
            print('{0} {1} {2} {3}'.format(m.group(1), m.group(2),
                m.group(3), m.group(4)))
