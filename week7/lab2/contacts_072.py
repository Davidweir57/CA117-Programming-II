#!/usr/bin/env python3

class Contact(object):

    def __init__(self, name, ph, email):
        self.name = name
        self.phone = ph
        self.email = email

    def __str__(self):
        return "{} {} {}".format(self.name, self.phone, self.email)

class ContactList(object):

    def __init__(self, d={}):
        self.d = {}

    def add_contact(self, con):
        self.d[con.name] = con

    def del_contact(self, name):
        if name in self.d:
            del self.d[name]

    def get_contact(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return "None"

    def __str__(self):
        conlist = []

        for (k, v) in sorted(self.d.items()):
            conlist.append("{}".format(v))

        return "Contact list" + "\n" + "-" * 12 + "\n" + "\n".join(conlist)
