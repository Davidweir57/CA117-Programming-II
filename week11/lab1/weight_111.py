class Weight(object):

    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.p = pounds
        self.o = ounces

    def from_ounces(weights):
        pounds = weights // 16
        ounces = weights % 16
        return Weight(pounds, ounces)

    def total_ounces(self):
         return (self.p * 16) + self.o

    def __str__(self):
        return "{} pound(s) and {} ounce(s)".format(self.p, self.o)

    def __eq__(self, other):
        return self.total_ounces() == other.total_ounces()

    def __lt__(self, other):
        return self.total_ounces() < other.total_ounces()

    def __gt__(self, other):
        return self.total_ounces() > other.total_ounces()

    def __ge__(self, other):
        return self.total_ounces() >= other.total_ounces()

    def __add__(self, other):
        added = self.total_ounces() + other.total_ounces()
        return Weight.from_ounces(added)

    def __iadd__(self, other):
        z = self + other
        self.p, self.o = z.p, z.o
        return self

    def __mul__(self, other):
        total = self.total_ounces() * other
        return Weight.from_ounces(total)
