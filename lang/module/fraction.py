#!/usr/bin/env python3

from fractions import Fraction
from functools import reduce
import operator


def product(fracs):
    t = reduce(operator.mul, fracs, 1)
    return t.numerator, t.denominator


if __name__ == '__main__':
    n = int(input())
    l = [Fraction(*map(int, input().split())) for _ in range(n)]
    print(*product(l))
