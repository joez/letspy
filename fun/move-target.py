#!/usr/bin/env python3


def move_target(items, target=0):
    k = 0
    for i, v in enumerate(items):
        if v != target:
            items[k] = v
            k += 1
    for i in range(k, len(items)):
        items[i] = target


if __name__ == '__main__':
    target = int(input())
    items = [int(x) for x in input().strip().split()]
    move_target(items, target)
    print(*items)
