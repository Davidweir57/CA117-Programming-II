#!/usr/bin/env python3

import sys

def sort(t):
    return t[-1]

def total(p):
    total = 0
    p = p.strip().split(",")
    for n in p:
        total = total + int(n)
    return total

def main():
    d = {}
    skips = []
    for line in sys.stdin:
        try:
            name, points = line.strip().split(":")
            totals = total(points)
            d[name] = totals
        except:
            skips.append(name)

    for (k, v) in sorted(d.items(), key=sort, reverse=True):
        print("{} : {}".format(k, v))
    print("Skipped:")
    for e in skips:
        print(e)


if __name__ == '__main__':
    main()
