#Atm lab Brandon Gonzalez

    # check_balance() returns the account balance
    # deposit(amount) deposits the given amount in the account
    # check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
    # withdraw(amount) withdraws the amount from the account and returns it
    # calc_interest() returns the amount of interest calculated on the account


import string
import math

class ATM:
    '''
    This class has multiple methods that allow the user to check the balance of their account and to modify their account. No data is saved after program run is complete.
    '''
    
    def __init__(self,balance = 0.00,interest = .01):
        '''
        Initializes the users balance, sets the banks interest rate for the account and creates a blank list that keeps track of the users actions within the program. 
        '''
        self.balance = balance
        self.interest = interest
        self.t_list = []
    
    def check_balance(self):
        self.t_list.append("User checked balance.")
        return (f"Your balance is ${self.balance}\n")
        
    def deposit(self,user_deposit):
        self.balance += user_deposit
        self.t_list.append(f"User made a deposit. New balance is ${self.balance}.")
        
    def withdraw(self, user_withdraw):
        if self.balance >= user_withdraw:
            self.balance -= user_withdraw
            self.t_list.append(f"User made a withdrawl. New balance is ${self.balance}.")
            return f"Your new balance is ${self.balance}\n"
        else:
            return("Insufficient Funds")
    def find_interest(self):
        total = self.balance + (self.balance * self.interest)
        self.t_list.append(f"User checked interest. New balance is ${self.balance+total}.")
        return (f"Your account balance with interest is ${round(total,2)}\n")
    def transactions(self):
        for t in self.t_list:
            print(t)
        
    
''' Program activation under a while loop, allowing the user to perform multiple functions. Checks are in place to preven invalid inputs and data is passed through the ATM class only'''
member_account = ATM()
while True:
    what_to_do = input("(1) to check balance\n(2) to make a deposit\n(3) to make a withdrawl\n(4) to check balance with interest\n(5) When transation complete.\n(6) To view transactions.\n:")
    if what_to_do == "1":
        print(member_account.check_balance())
    elif what_to_do == "2":
        amount_to_deposit = input("Type amount to deposit.\n:")
        amount_to_deposit = float(amount_to_deposit)
        member_account.deposit(amount_to_deposit)
    elif what_to_do == "3":
        amount_to_withdraw = input("How much would you like?\n:")
        amount_to_withdraw = float(amount_to_withdraw)
        print(member_account.withdraw(amount_to_withdraw))
    elif what_to_do == "4":
        print(f" Your balance with interest is {member_account.find_interest()}")
    elif what_to_do == "5":
        print(f"Your balance is {member_account.check_balance()}. Thank you, come again.")
        break
    elif what_to_do == "6":
        member_account.transactions()
    else:
        print("Invalid input.")
        continue
        
        