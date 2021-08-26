#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor, medication=[]):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.med = medication

    def __str__(self):
        return "Name: {}".format(self.name) + "\n" + "Age: {}".format(self.age) + "\n" + "Medications: {}".format(", ".join(self.med) + "\n" + "Doctor: {}".format(self.doctor))

class Ward(object):

    def __init__(self):
        self.w = {}

    def add(self, other):
        self.w[other.name] = other

    def remove(self, other):
        self.w.pop(other)

    def lookup(self, other):
        if other in self.w:
            return self.w[other]

    def get_patients_by_medication(self, other):
        l = []
        for Patient in self.w.values():
            if other in Patient.med:
                l.append(Patient)
        return l
