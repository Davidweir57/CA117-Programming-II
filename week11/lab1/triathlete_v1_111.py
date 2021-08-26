class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return "Name: {}".format(self.name) + "\n" + "ID: {}".format(self.tid)
