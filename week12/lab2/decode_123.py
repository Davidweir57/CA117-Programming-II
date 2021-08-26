#!/usr/bin/env python3

import sys

def main():
    vowels = "aeiou"
    for line in sys.stdin:
        line = [c for c in line.strip()]
        i = 0
        while i < len(line):
            if line[i] in vowels:
                line.pop(i + 1)
                line.pop(i + 1)
            i = i + 1
        print("".join(line))

if __name__ == '__main__':
    main()
