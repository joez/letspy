#!/usr/bin/env python3

# given a set A and n other sets.
# find whether set A is a strict superset of each of the n sets
# print True if yes, otherwise False

A = set(map(int, input().split()))
b = []
for _ in range(int(input())):
    b.append(A > set(map(int, input().split())))

print(all(b))
