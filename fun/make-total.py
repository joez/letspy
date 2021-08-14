#!/usr/bin/env python3

from itertools import product


def make_total(total, prices):
    max_factors = [int(total/x) for x in prices]
    for factors in product(*[range(f+1) for f in max_factors]):
        if total == sum([x*y for x, y in zip(factors, prices)]):
            return factors
    return None


if __name__ == '__main__':
    prices = list(map(int, input("Input prices: ").split()))
    totals = list(map(int, input("Input totals: ").split()))
    for total in totals:
        result = make_total(total, prices)
        output = " + ".join(f'{x}x{y}' for x,y in zip(result, prices) if x) if result else None
        print(f"{total}: {output}")
