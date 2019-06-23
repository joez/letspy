#!/usr/bin/env python3


def sprial_traverse(matrix):
    result = []
    while matrix and matrix[0]:
        if matrix[0]:
            result += matrix.pop(0)

        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        if matrix and matrix[-1]:
            result += matrix.pop()[::-1]

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result


matrix = [input().split() for _ in range(int(input()))]
print(*sprial_traverse(matrix))
