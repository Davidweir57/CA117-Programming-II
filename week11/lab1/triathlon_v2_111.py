class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

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

    def __str__(self):
        l = []
        for Triathlete in sorted(self.athl.values(), key=sort):
            l.append("Name: {}".format(Triathlete.name))
            l.append("ID: {}".format(Triathlete.tid))
        return "\n".join(l)
