#!/usr/bin/env python3


def reverse_words(s):
    return ' '.join(w[::-1] for w in s.split(' '))


def reverse_words_ext(s):
    # support other whitespaces
    strs, word = [], ''
    for c in s:
        if c.isspace():
            if word:
                strs.append(word[::-1])
                word = ''
            strs.append(c)
        else:
            word += c
    if word:
        strs.append(word[::-1])
    return ''.join(strs)


if __name__ == '__main__':
    s = input()
    for f in (reverse_words, reverse_words_ext):
        print(f(s))
