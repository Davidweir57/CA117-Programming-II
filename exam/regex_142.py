#!/usr/bin/env python3

import sys

from re import findall

def main():

    pattern = r'\b\d\d[xyz]\d{2,3}\s(?:cat|dog){2}\b'

    line = sys.stdin.readline().strip()

    match = findall(pattern, line)

    if len(match) == 1:
        print(match[0])

if __name__ == '__main__':
    main()