'''
Lab 22: ATM
Version 1

Let's represent an ATM with a class containing two attributes: a balance and an interest rate.
A newly created account will default to a balance of 0 and an interest rate of 0.1%.
Implement the initializer, as well as the following functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account
'''
class Atm:
    def __init__(self, bal=0, rate=0.001):
        self.bal = bal
        self.rate = rate

    def check_balance(self):
        return self.bal

    def deposit(self, amount):
        self.bal += amount

    def check_withdrawal(self, amount):
        if self.bal >= amount:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.bal -= amount

    def calc_interest(self):
        return self.bal * self.rate
