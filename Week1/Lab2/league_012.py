#!/usr/bin/env python3

import sys

def table(team):
    pos = team[0]
    club = team[1:-8]
    p = team[-8]
    w = team[-7]
    d = team[-6]
    l = team[-5]
    gf = team[-4]
    ga = team[-3]
    gd = team[-2]
    points = team[-1]

    club_name = ""
    club_name = " ".join(club)

    detail = [pos, club_name.lstrip(), p, w, d, l, gf, ga, gd, points]
    return detail

def main():
    h1 = "POS"
    h2 = "CLUB"
    h3 = "P"
    h4 = "W"
    h5 = "D"
    h6 = "L"
    h7 = "GF"
    h8 = "GA"
    h9 = "GD"
    h10 = "PTS"

    a = []
    t = []
    for line in sys.stdin:
        a = line.strip().split()
        t.append(table(a))

    i = 0
    longest = 0

    while i < len(t):
        name = t[i][1]

        if len(name) > longest:
            longest = len(name)
        i = i + 1

    print("{:>3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}".format(h1, h2, longest, h3, h4, h5, h6, h7, h8, h9, h10))

    i = 0
    while i < len(t):
        print("{:>3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}".format(t[i][0], t[i][1], longest, t[i][2], t[i][3], t[i][4], t[i][5], t[i][6], t[i][7], t[i][8], t[i][9]))
        i = i + 1

if __name__ == '__main__':
    main()
