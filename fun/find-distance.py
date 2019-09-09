#!/usr/bin/env python3


def find_distance(matrix, key):
    """Find the distance of the nearest key for each cell
    """
    if not matrix or not matrix[0]:
        return matrix

    rows, cols = len(matrix), len(matrix[0])
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def shortest(matrix, row, col, key):
        q = [(row, col, 0)]
        while q:
            r, c, d = q.pop(0)
            if matrix[r][c] == key:
                return d
            else:
                for i, j in delta:
                    nr, nc = r+i, c+j
                    if 0 <= nr < rows and 0 <= nc < cols:
                        q.append((nr, nc, d+1))

    result = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            result[r][c] = shortest(matrix, r, c, key)
    return result

if __name__ == '__main__':
    matrix = [input().split() for _ in range(int(input()))]
    print(find_distance(matrix, '0'))
