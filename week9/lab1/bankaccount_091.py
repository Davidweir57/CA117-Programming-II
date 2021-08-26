class BankAccount(object):

    next_account_number = 16555232
    account_type = "General"

    def __init__(self, forename, surname, balance):
        self.fname = forename
        self.sname = surname
        self.b = balance
        self.next_account_number = BankAccount.next_account_number
        BankAccount.next_account_number = BankAccount.next_account_number + 1

    def lodge(self, other):
        self.b = self.b + other
        return self

    def withdraw(self, other):
        if self.b - other >= 0:
            self.b = self.b - other
            return self
        else:
            print("Insufficient funds available")

    def __str__(self):
        return "Name: {} {}".format(self.fname, self.sname) + "\n" + "Account number: {}".format(self.next_account_number) + "\n" + "Account type: {}".format(BankAccount.account_type) + "\n" + "Balance: {:.2f}".format(self.b)

class CurrentAccount(BankAccount):

    overdraft = -1000.00
    account_type = "Current"

    def withdraw(self, other):
        if self.b - other >= CurrentAccount.overdraft:
            self.b = self.b - other
            return self
        else:
            print("Insufficient funds available")

    def __str__(self):
        return "Name: {} {}".format(self.fname, self.sname) + "\n" + "Account number: {}".format(self.next_account_number) + "\n" + "Account type: {}".format(CurrentAccount.account_type) + "\n" + "Balance: {:.2f}".format(self.b) + "\n" + "Overdraft: {:.2f}".format(CurrentAccount.overdraft)

class SavingsAccount(BankAccount):

    inteterest_rate = 0.01
    account_type = "Savings"

    def apply_interest(self):
        self.b = self.b + (self.b * SavingsAccount.inteterest_rate)
        return self

    def __str__(self):
        return "Name: {} {}".format(self.fname, self.sname) + "\n" + "Account number: {}".format(self.next_account_number) + "\n" + "Account type: {}".format(SavingsAccount.account_type) + "\n" + "Balance: {:.2f}".format(self.b) + "\n" + "Interest rate: {}".format(SavingsAccount.inteterest_rate)
