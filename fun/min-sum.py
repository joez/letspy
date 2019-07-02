#!/usr/bin/env python3


def min_sum(nums, target):
    '''
    find the minimal length of a contiguous subarray
    of which the sum >= target, return 0 if can't find

    >>> min_sum([1,2,2,4,2,2,2], 6)
    2
    '''
    size = 0
    total, s = 0, 0
    for i, v in enumerate(nums):
        total += v
        if total >= target:
            while total >= target:
                total -= nums[s]
                s += 1
            l = i - s + 1 + 1
            if size == 0 or l < size:
                size = l
    return size


if __name__ == "__main__":
    target = int(input())
    nums = [int(n) for n in input().split()]
    print(min_sum(nums, target))
