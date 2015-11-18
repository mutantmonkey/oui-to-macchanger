#!/usr/bin/python3

# Copyright © 2012 mutantmonkey <mutantmonkey@mutantmonkey.in>
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# the COPYING file for more details.

import re

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
