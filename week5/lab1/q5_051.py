#!/usr/bin/env python3

import sys

def sec(t):
    [mins, secs] = t.split(":")
    total = int(mins) * 60 + int(secs)
    return total

def sort(t):
    return sec(t[-1])

def main():
    d = {}
    for line in sys.stdin:
        try:
            tokens = line.strip().split()
            name, times = tokens[0], tokens[1:]
            d[name] = min(times, key=sec)
        except:
            continue

    winner = min(d.items(), key=sort)
    name, time = winner
    print("{} : {}".format(name, time))

if __name__ == '__main__':
    main()
