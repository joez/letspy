#!/usr/bin/env python3


def person_lister(fun):
    def inner(people):
        for p in sorted(people, key=lambda x: int(x[2])):
            yield fun(p)
    return inner


@person_lister
def name_format(p):
    return ("Mr. " if p[3] == "M" else "Ms. ") + p[0] + " " + p[1]


if __name__ == '__main__':
    people = [input().split() for _ in range(int(input()))]
    print(*name_format(people), sep='\n')
