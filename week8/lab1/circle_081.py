#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({:.1f}, {:.1f})".format(self.x, self.y)

    def midpoint(self, other):
        return ((self.x + other.x) / 2), ((self.y + other.y) / 2)

class Circle(object):

    def __init__(self, centre=Point(), radius=0):
        self.r = radius
        self.c = centre

    def __str__(self):
        return "Centre: {}".format(self.c) + "\n" + "Radius: {}".format(self.r)

    def __add__(self, other):
        return Circle(Point((self.c.x + other.c.x) / 2, (self.c.y + other.c.y) / 2), self.r + other.r)
