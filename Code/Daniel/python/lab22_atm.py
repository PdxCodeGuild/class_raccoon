import math

# default to a balance of 0 and an interest rate of 0.1%. Implement the initializer

class ATM:
    def __init__(self, balance = 0, int_rate = 0.1):
        self.balance = balance
        self.int_rate = int_rate

# check_balance() returns the account balance

    def check_bal(self):
        return self.balance       

# deposit(amount) deposits the given amount in the account

    def deposit(self, add):
        self.balance += add

# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative

    def check_with(self, check):
        if self.balance - check > 0:
            return True

# withdraw(amount) withdraws the amount from the account and returns it

    def withdraw(self, withdrawl):
        self.balance -= withdrawl

# calc_interest() returns the amount of interest calculated on the account 
    
    def check_int(self):
        return self.balance * self.int_rate


#actuall ATM part

while True:

    choice =  input("\n Would you like to check your balance, make a deposit, make a withdrawl, or quit?\n").lower()

    if "check" in choice:
        print(ATM.check_bal())
    


