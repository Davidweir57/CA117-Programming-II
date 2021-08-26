#!/usr/bin/env python3

import sys

def main():
    inputs = sys.stdin.read()
    points = inputs.strip().split()
    dx = 00
    dy = 0
    [ax, ay] = float(points[0]), float(points[1])
    [bx, by] = float(points[2]), float(points[3])
    [cx, cy] = float(points[4]), float(points[5])
    a_to_b = (((ax - bx) ** 2) + ((ay - by) ** 2)) ** 0.5
    a_to_c = (((ax - cx) ** 2) + ((ay - cy) ** 2)) ** 0.5
    b_to_c = (((bx - cx) ** 2) + ((by - cy) ** 2)) ** 0.5

    if a_to_b == a_to_c:
        #diag = b_to_c start point A
        mid = [((bx + cx) / 2), ((by + cy) / 2)]
        dx = (float(mid[0]) * 2) - float(ax)
        dy = (float(mid[1]) * 2) - float(ay)
    elif a_to_b == b_to_c:
        #diag = a to c start point B
        mid = [((ax + cx) / 2), ((ay + cy) / 2)]
        dx = (float(mid[0]) * 2) - float(bx)
        dy = (float(mid[1]) * 2) - float(by)
    else:
        #diag = a to b start point C
        mid = [((ax + bx) / 2), ((ay + by) / 2)]
        dx = (float(mid[0]) * 2) - float(cx)
        dy = (float(mid[1]) * 2) - float(cy)
    print(int(dx), int(dy))

if __name__ == '__main__':
    main()
