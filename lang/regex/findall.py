#!/usr/bin/env python3

import re

v = '[aeiou]'
c = '[qwrtypsdfghjklzxcvbnm]'
r = re.compile('(?<=' + c + ')' + v + '{2,}(?=' + c + ')', re.I)
print('\n'.join(r.findall(input()) or ['-1']))
