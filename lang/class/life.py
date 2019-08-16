#!/usr/bin/env python3

import random


class Life:
    def __init__(self):
        self.money = random.randint(0, 100)
        print(f'You born with {self.money} dollars')

    def work(self, *args):
        money = random.randint(0, 10)
        self.money += money
        print(f'You earn {money} dollars')

    def eat(self, *args):
        money = random.randint(0, 50)
        self.money -= money
        print(f'You spend {money} dollars')

    def sleep(self, *args):
        print(f'It is not allowed ;)')

    def die(self):
        print(f'You have {self.money} dollars left')
        print('Bye ...')
        exit(0)


if __name__ == '__main__':
    cmds = [m for m in vars(Life).keys() if not m.startswith('_')]
    print('Here is your life, you can: ' + ' '.join(cmds))
    life = Life()
    while True:
        cmd, *args = input('$ ').split()
        getattr(life, cmd, life.sleep)(*args)
