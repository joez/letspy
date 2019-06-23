#!/usr/bin/env python3

from operator import itemgetter
from textwrap import dedent


def feed():
    data = dedent('''\
        5 3
        10 2 5
        7 1 0
        9 9 9
        1 23 12
        6 5 9
        1
    ''')
    for l in data.split('\n'):
        yield l


i = iter(feed())
n, m = map(int, next(i).split())
data = [list(map(int, next(i).split())) for _ in range(n)]
k = int(next(i))

for r in sorted(data, key=itemgetter(k)):
    print(*r)
