class Shape(object):

    def __init__(self, points):
        self.points = points

    def sides(self):
        sides = []
        i = 0
        while i < len(self.points) - 1:
            distance = self.points[i].distance(self.points[i + 1])
            sides.append(distance)
            i = i + 1
        sides.append(self.points[0].distance(self.points[-1]))
        return sides

    def perimeter(self):
        return sum(self.sides())

class Point(Shape):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return (((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5)

class Triangle(Shape):

    def area(self):
        side = self.sides()
        s = sum(side) / 2
        a, b, c = side[0], side[1], side[2]
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area


class Square(Shape):

    def area(self):
        return self.sides()[0] ** 2
