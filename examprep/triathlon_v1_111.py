#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return "Name: {}".format(self.name) + "\n" + "ID: {}".format(self.tid)

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

from triathlon_v1_111 import Triathlete, Triathlon

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    tn.add(t1)
    tn.add(t2)

    t = tn.lookup(21)
    assert(isinstance(t, Triathlete))
    assert(t.name == 'Ian Brown')
    assert(t.tid == 21)

    tn.remove(21)
    t = tn.lookup(21)
    assert(t is None)

if __name__ == '__main__':
    main()
