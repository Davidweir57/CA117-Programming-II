#!/usr/bin/env python3

import sys

def check(s):
    word = ""
    for c in "evil":
        if s.lower().count(c) != 1:
            return False
    for c in s.lower():
        for l in "evil":
            if c in l:
                word = word + c
    if word == "evil":
        print(s)

def main():
    for lines in sys.stdin:
        word = lines.strip()
        check(word)

if __name__ == '__main__':
    main()
