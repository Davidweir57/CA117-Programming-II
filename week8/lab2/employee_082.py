class Employee(object):

    next_employee_number = 0

    def __init__(self, name, hourly_rate=9.25, hours_worked=0):
        self.name = name
        self.id = Employee.next_employee_number
        self.hourly = hourly_rate
        self.hours = hours_worked
        Employee.next_employee_number = Employee.next_employee_number + 1

    def add_hours(self, other):
        self.hours = self.hours + other
        return self

    def __str__(self):
        return "Name: {}".format(self.name) + "\n" + "ID: {}".format(self.id) + "\n" + "Hours: {:.2f}".format(self.hours) + "\n" + "Rate: {:.2f}".format(self.hourly) + "\n" + "Wages: {:.2f}".format(self.hours * self.hourly)
