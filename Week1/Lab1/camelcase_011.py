#!/usr/bin/env python3

import sys

def caps(s):
   i = 0
   while i < len(s):
      s[i] = s[i].capitalize()
      i = i + 1
   return " ".join(s)

def main():
    for line in sys.stdin:
        s = line.strip().split()
        print(caps(s))

if __name__ == '__main__':
    main()
