#!/usr/bin/env python3

import sys

def stars(lines, numl, numc):
    pixelslist = []

    for row in range(0, int(numl)):
        for col in range(0, int(numc)):
            if lines[row][col] == "-":
                pixelslist.append(str(row) + "-" + str(col))

    return pixelslist

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
    while starlist:
        e = starlist.pop()
        row, col = e[0], e[1]

        stack = []
        path = []

        stack.append(e)

        count = count + 1
        while stack:
            char = stack.pop()
            path.append(char)

            row, col = char.split('-')[0], char.split('-')[1]

            adjchars = [str(row) + "-" + str(int(col) - 1), str(row) + "-" + str(int(col) + 1), str(int(row) + 1) + "-" + str(col), str(int(row) - 1) + "-" + str(col)]
            new_list = [adjchar for adjchar in adjchars if adjchar in starlist]

            if len(new_list) > 0:
                stack.extend(new_list)

                for e in new_list:
                    starlist.remove(e)
    print(count)
if __name__ == '__main__':
   main()
