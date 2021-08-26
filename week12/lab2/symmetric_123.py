#!/usr/bin/env python3

import sys

def main():
    l1 = sys.stdin.read()
    l1 = l1.splitlines()
    l2 = []

    i = 0
    while i < len(l1):
        l2.append(l1[i])
        i = i + 2

    for e in l1:
        if e in l2:
            l1.pop(l1.index(e))
    l1 = sorted(l1, key=len, reverse=True)

    for e in l2:
        print(e)
    for e in l1:
        print(e)

if __name__ == '__main__':
    main()
