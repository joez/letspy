#!/usr/bin/env python3


def remove_duplicates(items):
    if len(items) < 1:
        return 0
    i, last = 0, items[0]
    for v in items[1:]:
        if last != v:
            i += 1
            items[i] = last = v
    return i+1


if __name__ == '__main__':
    items = input().strip().split()
    count = remove_duplicates(items)
    print(*items[:count])
