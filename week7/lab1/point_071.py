#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def reflect(self):
        self.x = self.x * -1
        self.y = self.y * -1

    def distance(self, other):
        x2, x1, y2, y1 = self.x, other.x, self.y, other.y
        dist = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
        return dist
