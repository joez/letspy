#!/usr/bin/env python3

import sys


def pascal_triangle(index):
    row = [1]
    for _ in range(index):
        row = [x + y for x, y in zip([0] + row, row + [0])]
    return row


if __name__ == '__main__':
    index = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(pascal_triangle(index))
