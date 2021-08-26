#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor, medication=[]):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.med = medication

    def add_medication(self, other):
        self.med.append(other)

    def __str__(self):
        return "Name: {}".format(self.name) + "\n" + "Age: {}".format(self.age) + "\n" + "Medications: {}".format(", ".join(self.med) + "\n" + "Doctor: {}".format(self.doctor))
