#!/usr/bin/env python3

import re

'''A valid postal code have to fullfil below requirements:

* It must be a number in the range from 100000 to 999999 inclusive
* It must not contain more than one alternating repetitive digit pair,
  two equal digits that have just a single digit between them
'''

p_range = re.compile(r'^[1-9]\d{5}$')
p_pair = re.compile(r'(\d)(?=\d\1)')

for _ in range(int(input())):
    code = input()
    print(bool(p_range.match(code)) and len(p_pair.findall(code)) < 2)
