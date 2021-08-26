#!/usr/bin/env python3

import sys

def sort(t):
    return t[-1]

def main():
    file = sys.argv[1]
    d = {}
    m = {}
    with open(file, "r") as f:
        for line in f:
            foods = line.strip().rsplit(" ", 1)
            d[foods[0]] = foods[1]
    for line in sys.stdin:
        total = 0
        tokens = line.strip().split(",")
        name, cal = tokens[0], tokens[1:]
        for food in cal:
            if food in d:
                total = total + int(d[food])
            else:
                total = total + 100
        m[name] = total
    maxn = len(max(m.keys(), key=len))
    maxm = len(str(max(m.values())))

    for (k, v) in sorted(m.items(), key=sort):
        print("{:>{}} : {:{}}".format(k, maxn, v, maxm))

if __name__ == '__main__':
    main()
