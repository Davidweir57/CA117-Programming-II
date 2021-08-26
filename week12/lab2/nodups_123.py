#!/usr/bin/env python3

import sys
import string
import re

def main():
    s = sys.stdin.read()
    cleaned = []
    exists = []
    s = re.findall(r'\S+|\n', s)

    for e in s:
        if e[-1] in string.punctuation:
            tmp = e[:-1]
        else:
            tmp = e

        if tmp.lower() not in (string.lower() for string in exists):
            if tmp != "\n":
                exists.append(tmp)
            cleaned.append(e)
        else:
            cleaned.append(".")

    print((" ".join(cleaned).replace(" \n ", "\n").rstrip(" \n")))

if __name__ == '__main__':
    main()
