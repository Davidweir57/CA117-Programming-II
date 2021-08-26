#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.t = {}

    def add_time(self, sport, time):
        self.t[sport] =  time

    def get_time(self, sport):
        return self.t[sport]

    def __eq__(self, other):
        return sum(self.t.values()) == other

    def __lt__(self, other):
        return sum(self.t.values()) < other

    def __gt__(self, other):
        return sum(self.t.values()) > other

    def __str__(self):
        return "Name: {}".format(self.name) + "\n" + "ID: {}".format(self.tid) + "\n" + "Race time: {}".format(sum(self.t.values()))

class Triathlon(object):

    def __init__(self):
        self.t = {}

    def add(self, other):
        self.t[other.tid] = other

    def remove(self, other):
        self.t.pop(other)

    def lookup(self, other):
        if other in self.t:
            return self.t[other]

    def best(self):
        return sorted(self.t.values())[0]

    def worst(self):
        return sorted(self.t.values())[-1]

    def __str__(self):
        l = []
        for Triathlete in sorted(self.t.values(), key=sort):
            l.append("Name: {}".format(Triathlete.name))
            l.append("ID: {}".format(Triathlete.tid))
        return "\n".join(l)

from triathlon_v3_111 import Triathlete, Triathlon

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)
    
    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()