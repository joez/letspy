#!/usr/bin/env python3

from collections import OrderedDict
from textwrap import dedent


def feed():
    data = dedent('''\
        9
        BANANA FRIES 12
        POTATO CHIPS 30
        APPLE JUICE 10
        CANDY 5
        APPLE JUICE 10
        CANDY 5
        CANDY 5
        CANDY 5
        POTATO CHIPS 30
    ''')
    for l in data.split('\n'):
        yield l


i = iter(feed())
n = int(next(i))
d = OrderedDict()

for _ in range(n):
    name, price = next(i).rsplit(maxsplit=1)
    d[name] = d.get(name, 0) + int(price)

for k, v in d.items():
    print(k, v)
