#!/usr/bin/env python3

import sys

def sort(t):
    return t[-1]

def main():
    double = {}
    for line in sys.stdin:
        count = []
        line = line.strip()
        count.append(line.count("aa"))
        count.append(line.count("ee"))
        count.append(line.count("ii"))
        count.append(line.count("oo"))
        count.append(line.count("uu"))
        double[line] = max(count)

    sorting = [(v, k) for k, v in double.items()]
    print(max(sorting)[1])

if __name__ == '__main__':
    main()
