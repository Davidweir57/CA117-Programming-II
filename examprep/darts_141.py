#!/usr/bin/env python3

import sys

def main():
    points = 0

    for line in sys.stdin:
        line = line.split()
        x, y = int(line[0]), int(line[1])
        dist = ((((0 - x) ** 2) + ((0 - y) ** 2)) ** 0.5)

        if dist > 200:
            points = points + 0
        elif 180 < dist <= 200:
            points = points + 1
        elif 160 < dist <= 180:
            points = points + 2
        elif 140 < dist <= 160:
            points = points + 3
        elif 120 < dist <= 140:
            points = points + 4
        elif 100 < dist <= 120:
            points = points + 5
        elif 80 < dist <= 100:
            points = points + 6
        elif 60 < dist <= 80:
            points = points + 7
        elif 40 < dist <= 60:
            points = points + 8
        elif 20 < dist <= 40:
            points = points + 9
        else:
            points = points + 10

    print(points)

if __name__ == '__main__':
    main()
