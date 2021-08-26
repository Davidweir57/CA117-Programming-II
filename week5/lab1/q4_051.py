#!/usr/bin/env python3

import sys

def mean(n, nums):
    mean = n / nums
    return mean

def median(l):
    l = sorted(l)
    mid = len(l) // 2
    if len(l) % 2 != 0:
        median = float(l[mid])
    else:
        median = (int(l[mid]) + int(l[mid - 1])) / 2
    return median

def main():
    total, count = 0, 0
    nums = []
    for line in sys.stdin:
        total = total + int(line)
        count += 1
        nums.append(line.strip())
    print("Mean: {:.1f}".format(mean(total, count)))
    print("Median: {:.1f}".format(median(nums)))

if __name__ == '__main__':
    main()
