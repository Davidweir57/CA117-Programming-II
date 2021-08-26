#!/usr/bin/env python3

import sys

def main():
    n = int(sys.argv[1])
    for c in range(1, 2 * n):
        spaces = abs(c - n)
        print(" " * spaces + "* " * (n - spaces - 1) + "*")

if __name__ == '__main__':
    main()
