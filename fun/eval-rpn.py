#!/usr/bin/env python3

import operator as op


def eval_rpn(tokens):
    ops = {
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': lambda a, b: int(a/b)
    }
    stack = []
    for t in tokens:
        if t in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[t](a, b))
        else:
            stack.append(int(t))
    return stack.pop()


if __name__ == '__main__':
    tokens = input('Reverse Polish Notation: ').split()
    result = eval_rpn(tokens)
    print('The result is: ' + str(result))