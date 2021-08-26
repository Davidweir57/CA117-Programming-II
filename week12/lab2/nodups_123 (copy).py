#!/usr/bin/env python3

import sys

def main():
    s = sys.stdin.read()
    cleaned = ""
    words = s.replace('.', ' .').split()

    for w in words:
        if w != "." and w.lower() in cleaned:
            w = "."
        elif w != ".":
            w = " " + w
        cleaned = cleaned + w
    print(cleaned)
    

if __name__ == '__main__':
    main()
