#!/usr/bin/env python3

import sys


def move(n, fr, aux, to):
    if n == 1:
        yield (fr, to)
    else:
        yield from move(n-1, fr, to, aux)
        yield from move(1, fr, aux, to)
        yield from move(n-1, aux, fr, to)


disks = int(sys.argv[1])
poles = ['A', 'B', 'C']
print(f'Towners of Hanoi with {str(disks)} disks and poles named', *poles)
for i, (fr, to) in enumerate(move(disks, *poles)):
    print(f'{i+1}: {fr} -> {to}')
