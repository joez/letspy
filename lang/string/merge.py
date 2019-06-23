#!/usr/bin/env python3


def merge_chars(string, block):
    for i in range(0, len(string), block):
        s = ''
        for c in string[i:i+block]:
            if c not in s:
                s += c
        print(s)


if __name__ == '__main__':
    merge_chars(input(), int(input()))
