#!/usr/bin/env python3


def rotate(nums, k):
    '''
    rotate the array to the right by k steps, k is non-negative
    '''
    n = len(nums)
    k = k % n
    for i, j in [(0, n-k-1), (n-k, n-1), (0, n-1)]:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i+1, j-1


if __name__ == "__main__":
    k = int(input())
    nums = [int(n) for n in input().split()]
    rotate(nums, k)
    print(nums)
