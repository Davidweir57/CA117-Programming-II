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

    def __str__(self):
        return "Name: {}".format(self.name) + "\n" + "ID: {}".format(self.tid) + "\n" + "Race time: {}".format(sum(self.t.values()))

from triathlete_v2_111 import Triathlete

def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)

if __name__ == '__main__':
    main()