#!/usr/bin/env python3

import sys

def main():
    pattern = "aeiou"
    for line in sys.stdin:
        words = [w for w in line.strip().lower() if w in pattern]
        if "".join(words) == pattern:
            print(line.strip())

if __name__ == '__main__':
    main()
