#!/usr/bin/env python3

import sys

def replace(w):
    for c in w:
        if c.islower():
            w = w.replace(c, "*")
    return w

def main():
    for line in sys.stdin:
        line = line.strip()
        lists = replace(line).split("*")
        print(max(lists, key=len))

if __name__ == '__main__':
    main()
