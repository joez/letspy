#!/usr/bin/env python3


def pivot_index(data):
    left, total = 0, sum(data)
    for i, v in enumerate(data):
        if left == total - left - v:
            return i
        left += v
    return -1


data = [int(x) for x in input().split()]
print(pivot_index(data))
