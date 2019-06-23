#!/usr/bin/env python3


def dominant_index(data):
    largest, index = max(data), 0
    for i, v in enumerate(data):
        if v == largest:
            index = i
        elif largest < v * 2:
            return -1
    return index

data = [int(x) for x in input().split()]
print(dominant_index(data))
