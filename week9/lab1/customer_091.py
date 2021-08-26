class Customer(object):

    discount = 0

    def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
        self.name = name
        self.b = balance
        self.addr1 = addr_line1
        self.addr2 = addr_line2
        self.addr3 = addr_line3

    def owes(self):
        return (self.b - ((self.b * self.discount) // 100))

    def __str__(self):
        return "{}".format(self.name) + "\n" + "{}".format(self.addr1) + "\n" + "{}".format(self.addr2) + "\n" + "{}".format(self.addr3) + "\n" + "Balance: {:.2f}".format(self.b) + "\n" + "Discount: {}%".format(self.discount) + "\n" + "Amount due: {:.2f}".format(self.owes())

class ValuedCustomer(Customer):
    discount = 10
