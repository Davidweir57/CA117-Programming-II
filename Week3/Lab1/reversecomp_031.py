#!/usr/bin/env python3

import sys

def bsearch(a, q):
   low = 0
   high = len(a)
   while low < high:
      mid = (low + high) // 2
      if a[mid] < q:
        low = mid + 1
      else:
        high = mid

   return a[low]

def main():
    words = []
    for line in sys.stdin:
      words.append(line.strip())
    words5 = sorted([w for w in words if len(w) >= 5])
    lwords = sorted([w.lower() for w in words5])
    print(sorted([w for w in words5 if bsearch(lwords, w[::-1].lower().strip()) == w[::-1].lower().strip() or w.lower() == w[::-1].lower()], key=str.lower))

if __name__ == '__main__':
    main()
