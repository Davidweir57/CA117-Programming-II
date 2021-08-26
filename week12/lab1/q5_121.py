#!/usr/bin/env python3

import sys

def sort(t):
    return t[-1]

def average(p):
    total = 0
    p = p.split(",")
    for e in p:
        if e.isdigit():
            total = total + int(e)
    average = total / 6
    return average

def main():
    d = {}
    for line in sys.stdin:
        line = line.strip()
        info = line.split(": ")
        name, points = info[0], info[1]
        averages = average(points)
        d[name] = averages

    for (k, v) in sorted(d.items(), key=sort, reverse=True):
        print("{}: {:.3}".format(k, v))

if __name__ == '__main__':
    main()
