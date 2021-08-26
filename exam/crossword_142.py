#!/usr/bin/env python3

import sys

def intersect(w1, w2):
    l1 = [c for c in w1]
    set1, set2 = set(w1), set(w2)
    shared = set1 & set2
    shared_list = [c for c in shared]

    intersect = l1.index(shared_list[0])
    for c in shared:
        if c in l1 and l1.index(c) < intersect:
            intersect = l1.index(c)
    return intersect


def main():
    for line in sys.stdin:
        line = line.split()
        w1, w2 = line[0], line[1]
        intersection = intersect(w1, w2)

        # loops i and j check to see if our current index is on
        # the same line or row as the intersection
        # i.e if it should be a character in word 1 or word 2
        for i in range(0, len(w2)):
            s = ""
            for j in range(0, len(w1)):
                if j == intersection:
                    s = s + w2[i]

                elif i == intersection:
                    s = s + w1[j]

                # if our current index is neither on the same row
                # or column as our intersection it is not part of
                # our 2 words (i.e it is not a letter) then we
                # print a "."
                else:
                    s = s + "."
            print(s)

if __name__ == '__main__':
    main()
