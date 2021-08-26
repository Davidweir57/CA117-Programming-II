#!/usr/bin/env python3

class Time(object):

    def __init__(self, hour=0, mins=0, sec=0):
        self.hour = hour
        self.min = mins
        self.sec = sec

    def __str__(self):
        return "The time is {:02}:{:02}:{:02}".format(self.hour, self.min, self.sec)

    def to_sec(self):
        return (self.hour * 60 * 60) + (self.min * 60) + self.sec

    def __eq__(self, other):
        return self.to_sec() == other.to_sec()

    def __gt__(self, other):
        return self.to_sec() > other.to_sec()

    def __lt__(self, other):
        return self.to_sec() < other.to_sec()

    def __add__(self, other):
        hour = self.hour + other.hour
        if hour > 24:
            hour = hour - 24
        mins = self.min + other.min
        if mins > 60:
            mins = mins - 60
            hour = hour + 1
        sec = self.sec + other.sec
        if sec > 60:
            sec = sec - 60
            mins = mins + 1
        return Time(hour, mins, sec)

    def __iadd__(self, other):
        z = self + other
        self.hour, self.min, self.sec = z.hour, z.min, z.sec
        return self

    @classmethod
    def seconds_to_time(cls, s):
        mins, sec = divmod(s, 60)
        hour, mins = divmod(mins, 60)
        overlflow, hour = divmod(hour, 24)
        return cls(hour, mins, sec)
