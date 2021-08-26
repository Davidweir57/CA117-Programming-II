#!/usr/bin/env python3

import sys
import string

d = {}

def main():
    text = sys.stdin.read().lower()
    freq = []
    vowels = "aeiou"
    for vowel in vowels:
        count = text.count(vowel)
        d[vowel] = count

    ml = 0
    for (k, v) in d.items():
        #print(v)
        if len(str(v)) > ml:
            ml = len(str(v))
    for (k, v) in sorted(d.items(), key=lambda item: item[1], reverse=True):
        print("{:>s} : {:{:d}d}".format(k, v, ml))

if __name__ == '__main__':
    main()
