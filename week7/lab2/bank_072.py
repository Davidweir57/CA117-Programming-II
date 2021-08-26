#!/usr/bin/env python3

class BankAccount(object):

    def __init__(self, balance=0):
        self.bal = int(balance)

    def deposit(self, deposit):
        self.bal = self.bal + int(deposit)

    def withdraw(self, withdrawn):
        if self.bal < int(withdrawn):
            print("Insufficient funds available")
        else:
            self.bal = self.bal - int(withdrawn)

    def __str__(self):
        return "Your current balance is: {:.2f} euro".format(self.bal)
