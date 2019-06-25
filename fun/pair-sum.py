#!/usr/bin/env python3


def pair_sum(nums, lo=-1000, hi=1000):
    '''
    Given an array of 2n integers, group these into n pairs, e.g. (a1, b1) ...
    which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
    Each integer is in the range of [-1000, 1000]

    >>> pair_sum([1,4,3,2])
    4
    '''
    bins = [0] * (hi - lo + 1)
    for n in nums:
        bins[n - lo] += 1

    total, odd = 0, True
    for i, v in enumerate(bins):
        while v > 0:
            if odd:
                total += lo + i
            odd = not odd
            v -= 1
    return total


nums = [int(n) for n in input().split()]
print(pair_sum(nums))
print(sum(sorted(nums)[::2]))
