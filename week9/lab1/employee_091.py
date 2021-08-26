class Employee(object):

    hours = 0
    rate = 0

    def __init__(self, name, number):
        self.name = name
        self.num = number

    def wages(self):
        return self.hours * self.rate

    def __str__(self):
        return "Name: {}".format(self.name) + "\n" + "Number: {}".format(self.num) + "\n" + "Wages: {:.2f}".format(self.wages())

class Manager(Employee):

    def __init__(self, name, number, salary):
        super().__init__(name, number)
        self.salary = salary

    def wages(self):
        return ((self.salary) / 52)

class AssemblyWorker(Employee):

    def __init__(self, name, number, hourly_rate, hours):
        super().__init__(name, number)
        self.hours = hours
        self.rate = hourly_rate

    def wages(self):
        return self.hours * self.rate
