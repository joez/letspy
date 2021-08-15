#!/usr/bin/env python3

from itertools import product
from functools import reduce


def gcd(a, b):
    if a < b:
        a, b = b, a
    while (b):
        a, b = b, a % b
    return a


def mgcd(nums):
    return reduce(gcd, nums)


def make_total(total, prices):
    max_factors = [total // x for x in prices]
    for factors in product(*[range(f + 1) for f in max_factors]):
        if total == sum([x * y for x, y in zip(factors, prices)]):
            return factors
    return None


if __name__ == '__main__':
    prices = list(reversed(sorted(map(int, input("Input prices: ").split()))))
    totals = list(map(int, input("Input totals: ").split()))
    common = mgcd(prices)
    if common > 1:
        prices = [x // common for x in prices]
        # no solution if total can't be divided by common
        totals = [x // common if x % common else None for x in totals]
    for total in totals:
        result = make_total(total, prices) if total else None
        output = " + ".join(f'{x}x{y}' for x,y in zip(result, prices) if x) if result else None
        print(f"{total}: {output}")
