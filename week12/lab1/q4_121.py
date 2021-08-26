#!/usr/bin/env python3

import sys
from re import findall

def main():
    for line in sys.stdin:
        line = line.strip()
        line = findall(r'[A-Z][^A-Z]*', line)

        i = 1
        while i < len(line):
            e = line[i]
            e = e.lower()
            line[i] = e
            i = i + 1

        print(" ".join(line))

if __name__ == '__main__':
    main()
