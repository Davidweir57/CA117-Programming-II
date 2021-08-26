class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.t = {}

    def __eq__(self, other):
        return sum(self.t.values()) == other

    def __lt__(self, other):
        return sum(self.t.values()) < other

    def __gt__(self, other):
        return sum(self.t.values()) > other

    def add_time(self, sport, t):
        self.t[sport] = t

    def get_time(self, sport):
        return self.t[sport]

    def __str__(self):
        return "Name: {}".format(self.name) + "\n" + "ID: {}".format(self.tid) + "\n" + "Race time: {}".format(sum(self.t.values()))

def sort(t):
        return t.name

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

    def best(self):
        return sorted(self.athl.values())[0]

    def worst(self):
        return sorted(self.athl.values())[-1]

    def __str__(self):
        l = []
        for Triathlete in sorted(self.athl.values(), key=sort):
            l.append("Name: {}".format(Triathlete.name))
            l.append("ID: {}".format(Triathlete.tid))
        return "\n".join(l)
