#!/usr/bin/env python3

import sys

def main():
    s = sys.argv[1]
    N = int(sys.argv[2])

    s = [c for c in s.strip()]
    i = 0
    while i < N:
        tmp = s[0]
        s.pop(0)
        s.insert(len(s), tmp)
        i = i + 1

    print("".join(s))

if __name__ == '__main__':
    main()
