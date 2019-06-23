#!/usr/bin/env python3


def plus_one(data):
    carry = 1
    for i in range(len(data)-1, -1, -1):
        if data[i] + carry == 10:
            data[i], carry = 0, 1
        else:
            data[i] += carry
            carry = 0
            break
    if carry > 0:
        data.insert(0, carry)
    return data


data = [int(x) for x in input().split()]
print(plus_one(data))
