#!/usr/bin/env python3

import sys

def main():
    lines = []
    index = []
    for line in sys.stdin:
        line = line.split()
        row = [c for c in line]
        lines.append(row)

    l1 = lines[0]
    l2 = lines[1]

    i = 0
    while i < len(l1) and len(l2):
        if l1[i] == l2[i]:
            index.append(i)
        i = i + 1

    print(index)

if __name__ == '__main__':
    main()
