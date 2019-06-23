#!/usr/bin/env python3


def diagonal_traverse(matrix):
    m, n = len(matrix), len(matrix[0])
    diag = [[] for _ in range(m + n - 1)]
    for c in range(n):
        for r in range(m):
            diag[r+c].append(matrix[r][c])
    return diag


matrix = [input().split() for _ in range(int(input()))]
result = diagonal_traverse(matrix)

print('diagonal:')
data = []
for v in result:
    data += v
print(*data)

print('zigzag:')
data = []
for i, v in enumerate(result):
    data += v if i % 2 == 0 else reversed(v)
print(*data)
