#!/usr/bin/env python3


def longest_prefix(strs):
    prefix = min(strs, key=len)
    for i, c in enumerate(prefix):
        for s in strs:
            if s[i] != c:
                return prefix[:i]
    return prefix


def another_solution(strs):
    prefix = ''
    for l in zip(*strs):
        if len(set(l)) == 1:
            prefix += l[0]
        else:
            break
    return prefix


strs = [input() for _ in range(int(input()))]
for f in (longest_prefix, another_solution):
    print(f(strs))
