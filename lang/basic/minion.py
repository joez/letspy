#!/usr/bin/env python3


def minion_game(s):
    vowels = set('AEIOU')
    kevsc, stusc = 0, 0
    for i in range(len(s)):
        count = len(s) - 1 - i + 1
        if s[i] in vowels:
            kevsc += count
        else:
            stusc += count

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")


if __name__ == '__main__':
    minion_game(input())
