#!/usr/bin/env python3


class MinStack:
    def __init__(self):
        self.data = []
        self.mini = []

    def push(self, d):
        self.data.append(d)
        if len(self.mini) == 0 or d <= self.mini[-1]:
            self.mini.append(d)

    def pop(self):
        d = self.data.pop()
        if d == self.mini[-1]:
            self.mini.pop()
        return d

    @property
    def min(self):
        return self.mini[-1]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]


if __name__ == '__main__':
    stack = MinStack()
    for d in map(int, input().split()):
        stack.push(d)
    for _ in range(len(stack)):
        print(f'top: {stack[-1]}, min: {stack.min}')
        stack.pop()
