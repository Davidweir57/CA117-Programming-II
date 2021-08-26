class Student(object):

    def __init__(self, sname, fname, sid, modlist=[]):
        self.sname = sname
        self.fname = fname
        self.sid = sid
        self.modlist = modlist

    def add_module(self, mod):
        self.modlist.append(mod)

    def del_module(self, mod):
        if mod in self.modlist:
            self.modlist.remove(mod)

    def print_details(self):
        print("ID: {}".format(self.sid))
        print("Surname: {}".format(self.sname))
        print("Forename: {}".format(self.fname))
        print("Modules: {}".format(" ".join(self.modlist)))
