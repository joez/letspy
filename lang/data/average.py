#!/usr/bin/env python3

from collections import namedtuple


def oneline():
    data = '''5
    ID         MARKS      NAME       CLASS
    1          97         Raymond    7
    2          50         Steven     4
    3          91         Adrian     9
    4          72         Stewart    5
    5          80         Peter      6
    '''
    for l in data.split('\n'):
        yield l.strip()


i = iter(oneline())
n = int(next(i))
R = namedtuple('R', next(i))
average = sum(int(R(*next(i).split()).MARKS) for _ in range(n)) / n
print(f"The average marks: {average}")
