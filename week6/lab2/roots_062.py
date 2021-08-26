#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        line = line.strip().split()
        a, b, c = int(line[0]), int(line[1]), int(line[2])
        check = ((b ** 2) - 4 * a * c)
        div = 2 * a
        if check >= 0:
            r1 = ((-b) + ((b ** 2) - (4 * a * c)) ** 0.5) / div
            r2 = ((-b) - ((b ** 2) - 4 * a * c) ** 0.5) / div
            print("r1 = {}, r2 = {}".format(r1, r2))
        else:
            print("None")

if __name__ == '__main__':
    main()
