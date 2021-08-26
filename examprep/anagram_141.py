#!/usr/bin/env python3

import sys

def anagram(a, b):
    for c in a:
        if c not in b:
            return False
        b = b.replace(c, '', 1)
    return True

def main():
    a, b = sys.stdin.readline().strip().split()

    print(anagram(a, b))

if __name__ == '__main__':
    main()