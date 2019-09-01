#!/usr/bin/env python3


def is_balanced(s, pairs='[]{}()'):
    l, r, match = set(), set(), {}
    for k, v in zip(*[iter(pairs)]*2):
        match[k] = v
        l.add(k)
        r.add(v)
    stack = []
    for c in s:
        if c in l:
            stack.append(c)
        elif c in r:
            if not stack or c != match[stack.pop()]:
                return False
    return False if stack else True


if __name__ == '__main__':
    for _ in range(int(input())):
        print(is_balanced(input()))
