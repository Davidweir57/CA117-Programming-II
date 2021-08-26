#!/usr/bin/env python3

import sys

def centre(a, spaces):
    i = 0
    while i < len(a):
        lines = a[i]
        print("{:^{}s}".format(lines, spaces))
        i = i + 1

def main():
    a = []
    for line in sys.stdin:
        line = line.strip()
        a.append(line)

    longest = 0
    i = 0
    while i < len(a):
        if len(a[i]) > longest:
            longest = len(a[i])
        i = i + 1
    return(centre(a, longest))

if __name__ == '__main__':
    main()
