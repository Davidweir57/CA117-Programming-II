#!/usr/bin/env python3

import sys

def main():
    for lines in sys.stdin:
        char = lines.strip()
        try:
            check = int(char) / 2
            print("Thank you for " + char)
            break
        except:
            print(char + " " + "is not a number")

if __name__ == '__main__':
    main()
