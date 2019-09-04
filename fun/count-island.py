#!/usr/bin/env python3


def count_islands(grid):
    if not grid:
        return 0

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (up, down, left, right)
    rows, cols = len(grid), len(grid[0])
    count = 0

    def flood(grid, row, col):
        grid[row][col] = '0'
        for r, c in [(row+i, col+j) for i, j in delta]:
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
                flood(grid, r, c)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                count += 1
                flood(grid, row, col)

    return count


grid = [input().split() for _ in range(int(input()))]
print('Total {:d} islands'.format(count_islands(grid)))
