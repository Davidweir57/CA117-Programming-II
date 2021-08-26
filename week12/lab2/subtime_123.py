#!/usr/bin/env python3

import sys

def hr_to_min(n):
    return n * 60

def min_to_24hr(t):
    time = []
    h = t // 60
    m = t - (hr_to_min(h))
    time.append(h)
    time.append(m)
    return time


def main():
    for line in sys.stdin:
        line = line.split()
        time, amount = line[0], int(line[1])

        time = time.split(":")
        h, m = int(time[0]), int(time[1])
        time = hr_to_min(h) + m
        if amount > 0:
            time = time - amount
            time = min_to_24hr(time)
            hr = 24 + int(time[0])
            min = time[1]
            if hr == 24:
                hr = "00"
            print("{}:{:>02}".format(hr, str(min)))
        else:
            time = time + (amount * -1)
            time = min_to_24hr(time)
            hr, min = time[0], time[1]
            if hr == 24:
                hr = "00"
                print("{}:{:>02}".format(hr, str(min)))

if __name__ == '__main__':
    main()
