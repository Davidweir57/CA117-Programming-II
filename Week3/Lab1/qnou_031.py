#!/usr/bin/env python3

import sys

def qnou(words):
    return [w.strip() for w in words if w.lower().count("q") > w.lower().count("qu")]

def main():
    words = []
    for lines in sys.stdin:
        words.append(lines)
    print("Words with q but no u:", qnou(words))


if __name__ == '__main__':
    main()
