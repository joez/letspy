#!/usr/bin/env python3

import itertools
import math


def candidates(elements):
    if len(elements) < 2:
        yield elements[0]
        return
    skip = set()  # to skip logically duplicated ones
    for x, y, *rest in itertools.permutations(elements):
        for op in '+-*/':  # supported operations
            pair = frozenset([x, y, op])
            if pair in skip:
                continue
            expr = f'({x} {op} {y})' if rest else f'{x} {op} {y}'
            yield from candidates([expr] + rest)
            if op in '+*':  # commutative property，e.g. x+y=y+x
                skip.add(pair)
            else:
                if x == y:  # special cases: x-x=0, x/x=1
                    skip.add(pair)


def isvalid(expression, target=24):
    try:  # we evaluate the expression in foat point math
        if math.isclose(eval(expression), target):
            return True
    except ZeroDivisionError:
        pass
    return False


if __name__ == '__main__':
    while True:
        try:
            cards = input("Input cards (CTRL+C to quit): ").split()
            seen = set()  # to skip duplicated ones
            for e in candidates(cards):
                if e not in seen and isvalid(e):
                    print('.', flush=True, end='')  # we are working
                    seen.add(e)
            print("\nSolutions:") if len(seen) else print('No solution')
            for e in sorted(seen):
                print(e)
        except KeyboardInterrupt:
            break
