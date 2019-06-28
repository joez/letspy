#!/usr/bin/env python3


def max_consecutive(nums, target):
    '''
    Given an array, find the maximum number of consecutive target

    >>> max_consecutive([1,2,2,4,2,2,2], 2)
    3
    '''
    prev, curr = 0, 0
    for n in nums:
        if n == target:
            curr += 1
        else:
            prev, curr = max(prev, curr), 0
    return max(prev, curr)


if __name__ == "__main__":
    target = int(input())
    nums = [int(n) for n in input().split()]
    print(max_consecutive(nums, target))
