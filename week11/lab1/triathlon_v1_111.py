class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return "Name: {}".format(self.name) + "\n" + "ID: {}".format(self.tid)

class Triathlon(object):

    def __init__(self):
        self.athl = {}

    def add(self, other):
        self.athl[other.tid] = other

    def remove(self, other):
        self.athl.pop(other)

    def lookup(self, other):
        if other in self.athl:
            return self.athl[other]
