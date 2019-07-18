#!/usr/bin/env python3

import random


def guess(words, health=8):
    secret = random.choice(words)
    done, todo = set(), set(secret)
    while health > 0:
        guess = input("Guess a letter: ")
        right = guess in todo
        if right:
            done.add(guess)
        else:
            health -= 1
        is_in = 'in' if right else 'not in'
        print('"{}" is {} the word.'.format(guess, is_in))
        print(f'Health points = {health:d}')
        if done == todo:
            print(f'Congratulations, you did it! The word is {secret}')
            break


if __name__ == '__main__':
    words = input("Candidate words to guess: ").split()
    health = int(input("Maximum health points: "))
    print("Now let's guess!")
    guess(words, health)
