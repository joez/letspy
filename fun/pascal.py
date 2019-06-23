#!/usr/bin/env python3

import sys


def pascal_triangle(rows):
    matrix = []
    for r in range(rows):
        row = [1] * (r + 1)
        for c in range(1, r):
            p = matrix[r-1]
            row[c] = p[c-1] + p[c]
        matrix.append(row)
    return matrix


if __name__ == '__main__':
    rows = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    matrix = pascal_triangle(rows)
    output = [' '.join(map(str, r)) for r in matrix]
    width = max(len(r) for r in output)
    for r in output:
        print(r.center(width))
