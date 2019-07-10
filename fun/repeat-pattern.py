#!/usr/bin/env python3

from itertools import cycle


def repeat_pattern(pattern, offset, length):
    p = zip(cycle(pattern), range(length))
    return ' ' * offset + ''.join(x for x, _ in p)


if __name__ == "__main__":
    pattern = input()
    for offset, length in zip(*([map(int, input().split())] * 2)):
        print(repeat_pattern(pattern, offset, length))
