#!/usr/bin/env python3

import sys

def main():
    word = sys.argv[1]
    chars = [c for c in word]
    for i in range(0, len(chars) - 1, 2):
        tmp = chars[i]
        chars[i] = chars[i + 1]
        chars[i + 1] = tmp
    print("".join(chars))

if __name__ == '__main__':
    main()
