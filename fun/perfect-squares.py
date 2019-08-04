#!/usr/bin/env python3

from math import sqrt

# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.


def squares(target):
    sqrts = set((i+1)**2 for i in range(int(sqrt(target))))
    count, goals = 1, {target}
    while goals:
        next_goals = set()
        for g in goals:
            if g in sqrts:
                return count
            for s in sqrts:
                r = g - s
                if r in sqrts:
                    return count + 1
                elif r > 0:
                    next_goals.add(r)
        count += 1
        goals = next_goals
    return count


if __name__ == '__main__':
    target = int(input("Target: "))
    count = squares(target)
    print(f'{count:d} perfect square numbers sum to {target:d}')
