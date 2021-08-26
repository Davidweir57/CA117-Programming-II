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
        if len(w) > 3:
            count = ntext.count(w)
            if count >= 3:
                d[w] = count
    for (k, v) in sorted(d.items()):
        maxk = len(max(d.keys(), key=len))
        print("{:>{:d}s} : {:{:d}d}".format(k, maxk, v, 2))

if __name__ == '__main__':
    main()
