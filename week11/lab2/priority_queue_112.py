class PQ(object):

    def __init__(self):
        self.d = {}
        self.N = 0

    def insert(self, e):
        self.N = self.N + 1
        self.d[self.N] = e
        self.swim(self.N)

    def swim(self, v):
        while v > 1 and self.d[v] > self.d[v // 2]:
            self.exch(v, v // 2)
            v = v // 2

    def exch(self, i, j):
        self.d[i], self.d[j] = self.d[j], self.d[i]

    def size(self):
        return self.N

    def is_empty(self):
        return self.N == 0

    def getMax(self):
        return self.d[1]

    def bigger(self, i, j):
        try:
            return max([i, j], key=self.d.__getitem__)
        except:
            return i

    def sink(self, v):
        while v * 2 <= self.N:
            child = v * 2
            child = self.bigger(child, child + 1)
            if self.d[v] >= self.d[child]:
                break
            self.exch(v, child)
            v = child

    def delMax(self):
        max = self.d[1]
        self.exch(1, self.N)
        del(self.d[self.N])
        self.N = self.N - 1
        self.sink(1)
        return max
