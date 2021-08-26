#!/usr/bin/env python3

import sys
import string

d = {}

def punc(s):
    for c in s:
        if c in string.punctuation and c != "'":
            s = s.replace(c, "")
    return s

def main():
    text = sys.stdin.read()
    ntext = punc(text).lower().split()
    for w in ntext:
        count = ntext.count(w)
        d[w] = count
    for (k, v) in sorted(d.items()):
        print("{} : {}".format(k, v))

if __name__ == '__main__':
    main()
