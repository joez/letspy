#!/usr/bin/env python3


def add_binary(a, b):
    if len(a) < len(b):
        a, b = b, a
    result, carry = [], 0
    for i in range(len(a)):
        va = int(a[-(i+1)])
        vb = int(b[-(i+1)]) if i < len(b) else 0
        carry, v = divmod(va + vb + carry, 2)
        result.append(v)
    if carry:
        result.append(carry)
    return ''.join(map(str, reversed(result)))


a, b = input().split()
print(add_binary(a, b))
print(format(int(a, 2) + int(b, 2), 'b'))