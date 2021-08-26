#!/usr/bin/env python3

import sys

nums = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
}

trans = {}

def main():
    with open(sys.argv[1], "r") as f:
        for line in f:
            eng, irish = line.strip().split()
            trans[eng] = irish
    for num in sys.stdin:
        line = ""
        numbers = num.strip().split()
        for c in numbers:
            if c in nums:
                line = line + trans[nums[c]] + " "
        print(line[:-1])

if __name__ == '__main__':
    main()
