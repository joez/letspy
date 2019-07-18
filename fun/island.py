#!/usr/bin/env python3

from collections import OrderedDict

def count_islands(grid):
    rows, cols = len(grid), len(grid[0])
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (up, down, left, right)
    count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                count += 1
                # clear adjacent ones with BFS
                queue = OrderedDict()
                queue[(row, col)] = 1
                while queue:
                    (r, c), _ = queue.popitem(False)
                    grid[r][c] = '0'
                    for i, j in ((r+i, c+j) for i, j in delta):
                        if 0 <= i < rows and 0 <= j < cols and grid[i][j] == '1':
                            queue[(i, j)] = 1
    return count


grid = [input().split() for _ in range(int(input()))]
print('Total {:d} islands'.format(count_islands(grid)))
