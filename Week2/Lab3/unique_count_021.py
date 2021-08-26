#!/usr/bin/env python3

import sys
import string


def alpha_num(s):
    l = []
    for c in s:
        if c.isalnum():
            l.append(c)
    return l

def unique(words):
    a = []
    i = 0
    count = 0

    for k in words:
        if k not in a:
            a.append(k)
    return(a)

def main():
    count = 0
    uniquelist = []
    lines = sys.stdin.read()
    words = lines.strip().lower()
    for c in words:
        if c in string.punctuation:
            words = words.replace(c, "")
    words = words.split()

    words = alpha_num(words)
    uniquelist = (unique(words))
    count = count + len(uniquelist)
    print(count)

if __name__ == '__main__':
    main()
