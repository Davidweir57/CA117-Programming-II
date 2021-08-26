class BankAccount(object):

    next_account_number = 16555232

    total_lodgements = 0

    interest_rate = 0.043

    def __init__(self, forename, surname, balance=0):
        self.fname = forename
        self.sname = surname
        self.balance = balance
        self.num = BankAccount.next_account_number
        BankAccount.next_account_number = BankAccount.next_account_number + 1
        BankAccount.total_lodgements = BankAccount.total_lodgements + 1

    def lodge(self, other):
        self.balance = self.balance + other
        BankAccount.total_lodgements = BankAccount.total_lodgements + 1
        return self

    def apply_interest(self):
        intr = self.balance * BankAccount.interest_rate
        self.balance = self.balance + intr
        return self

    def __iadd__(self, other):
        self.balance = self.balance + other
        return self

    def __str__(self):
        return "Name: {} {}".format(self.fname, self.sname) + "\n" + "Account number: {}".format(self.num) + "\n" + "Balance: {:.2f}".format(self.balance)
