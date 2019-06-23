#!/usr/bin/env python3

n, x = map(int, input().split())
mark = [map(float, input().split()) for _ in range(x)]
for m in zip(*mark):
    print('{:.1f}'.format(sum(m)/x))
