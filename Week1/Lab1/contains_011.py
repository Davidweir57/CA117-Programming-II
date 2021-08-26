#!/usr/bin/env python3

import sys

def contains(char, s):
    for c in char:
        if c in s:
            s = s.replace(c, "", 1)
        else:
            return False
    return True

def main():
    for line in sys.stdin:
        [char, s] = line.lower().strip().split()
        print(contains(char, s))


if __name__ == '__main__':
    main()
