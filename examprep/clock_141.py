#!/usr/bin/env python3

import sys

def main():
    s = sys.stdin.read()
    s = s.split()
    t1, t2 = int(s[0]), int(s[1])

    if t1 > t2:
        aclk = t2 - t1
        clk = t2 + (12 - t1)
        if abs(aclk) < abs(clk):
            print(aclk)
        else:
            print(clk)
    else:
        clk = t2 - t1
        aclk = t2 + (12 - t1)
        if abs(aclk) < abs(clk):
            print(aclk)
        else:
            print(clk)


if __name__ == '__main__':
    main()
