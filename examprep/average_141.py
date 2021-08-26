#!/usr/bin/env python3

import sys

def average(l):
    total = 0
    for e in l:
        total = total + len(e)
    return total / len(l)

def main():
    words = sys.stdin.read()
    words = words.split()
    print("Average: {:.2f}".format(average(words)))

    above = []
    for e in words:
        if len(e) > average(words):
            above.append(e)

    for w in above:
        print(w)

if __name__ == '__main__':
    main()
