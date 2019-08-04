#!/usr/bin/env python3

from collections import deque


def unlock(target, deadends):
    delta = {str(i): [str((i+1) % 10), str((i-1) % 10)] for i in range(10)}

    def next_steps(current):
        for i, v in enumerate(current):
            for n in delta[v]:
                yield current[:i] + n + current[i+1:]
    steps, visited = 0, set(deadends)
    queue = deque([('0000', 0)])
    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        elif current not in visited:
            visited.add(current)
            for n in next_steps(current):
                queue.append((n, steps+1))
    return -1


if __name__ == '__main__':
    print('Unlock a lock with several circular wheels')
    target = input("Target code: ")
    deadends = input("Dead ends: ").split()
    steps = unlock(target, deadends)
    print(f'Total {steps:d} steps are needed')
