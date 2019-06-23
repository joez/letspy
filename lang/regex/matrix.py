#!/usr/bin/env python3

import re

n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

result = ''
for c in zip(*matrix):
    result += "".join(c)

print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', result))
