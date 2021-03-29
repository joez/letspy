#!/usr/bin/env python3

import sys
import random


def gen_grid(rows=4, cols=4):
    '''
    Generate a Schulte Grid with given cols and rows
    The result is a 2D array (list of rows)
    '''
    nums = list(range(1, cols * rows + 1))
    random.shuffle(nums)
    grid = [None] * rows
    for r in range(0, len(grid)):
        grid[r], nums = nums[:cols], nums[cols:]
    return grid


if __name__ == "__main__":
    rows = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    cols = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    grid = gen_grid(rows=rows, cols=cols)
    [print(*row) for row in grid]
