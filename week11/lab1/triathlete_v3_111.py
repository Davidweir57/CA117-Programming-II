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
