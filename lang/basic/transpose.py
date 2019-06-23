#!/usr/bin/env python3


def transpose(matrix):
    return [list(col) for col in zip(*matrix)]


matrix = [input().split() for _ in range(int(input()))]
for row in transpose(matrix):
    print(*row)
