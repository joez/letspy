#!/usr/bin/env python3


def two_sum(nums, target):
    '''
    Given an array of integers that is already sorted in ascending order,
    find two numbers that they add up to the target, and return the index.
    You can assume that each input would have exactly one solution.

    >>> two_sum([1,2,3,4,5,9], 9)
    (3, 4)
    '''
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s > target:
            j -= 1
        elif s < target:
            i += 1
        else:
            break
    return i, j


if __name__ == "__main__":
    import os
    if os.environ.get('TEST'):
        import doctest
        doctest.testmod()
    else:
        target = int(input())
        nums = [int(n) for n in input().split()]
        print(two_sum(list(sorted(nums)), target))
