#!/usr/bin/env python3

import re

'''
A valid UID must follow the rules below:

* It must contain at least 2 uppercase English alphabet characters
* It must contain at least 3 digits
* It should only contain alphanumeric characters
* No character should repeat
* There must be exactly 10 characters in a valid UID
'''

p = re.compile(r'^[a-zA-Z\d]{10}$')
m = [(re.compile(r'[A-Z]'), 2), (re.compile(r'\d'), 3)]
f = lambda s, p, c: len(p.findall(s)) >= c
for _ in range(int(input())):
    uid = input().strip()
    res = p.match(uid) and len(uid) == len(set(uid))
    res = res and all(f(uid, p, c) for p, c in m)
    print('Valid' if res else 'Invalid')
