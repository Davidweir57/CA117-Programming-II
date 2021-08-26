#!/usr/bin/env python3

import sys

def stars(lines, numl, numc):
    starlist = []
    for rows in range(0, 99):
        for col in range(0, 100):
            if lines[rows][col] == "-":
                starlist.append([rows, col])
    return starlist

def main():
    s = sys.stdin.readline().split()
    numl = s[0]
    numc = s[1]

    lines = []
    for line in sys.stdin:
        line = line.strip()
        line = [c for c in line]
        lines.append(line)

    starlist = stars(lines, numl, numc)

    count = 0
    for e in starlist:
        row, col = e[0], e[1]

        stack = []
        path = [] #stores all elements that make up a star >= 1 "-"

        stack.append(e)
        ind = starlist.index(e)
        starlist[ind] = [-1, -1]

        if e[0] != -1 and e[1] != -1:
            count = count + 1
            while stack:
                char = stack.pop()
                path.append(char)

                row, col = char[0], char[1]
                adjchars = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]

                for adjchar in adjchars:
                    if adjchar in starlist:
                        stack.append(adjchar)
                        ind = starlist.index(adjchar)
                        starlist[ind] = [-1, -1]
    print(count)

if __name__ == '__main__':
    main()
