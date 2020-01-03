'''
Filename: lab22_atm.py
Author: Dylan
Purpose: Create atm class
'''

import helper


class ATM:
    def __init__(self,name,balance = 0.00,interest=.1):
        self.balance = balance
        self.interest = interest
        self.transactions = []
        self.cont = "y"
        self.name = name

    def check_balance(self): 
        print(f"Your balance is {'${:,.2f}'.format(self.balance)}.")

    def deposit(self):
        amount = float(helper.float_checker(input("How much would you like to deposit? \n> ")))
        self.balance += amount
        self.transactions.append(f"You have deposited {'${:,.2f}'.format(amount)}. Your balance is now {'${:,.2f}'.format(self.balance)}.")
        print(self.transactions[-1])

    def check_withdrawal(self,amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def withdraw(self):
        amount = float(helper.float_checker(input("How much would you like to withdraw? \n> ")))
        if self.check_withdrawal(amount):
            self.balance -= amount
            self.transactions.append(f"You have withdrawn {'${:,.2f}'.format(amount)}. Your balance is {'${:,.2f}'.format(self.balance)}.")
            print(self.transactions[-1])
        else:
            print(f"ERROR: Your balance is {'${:,.2f}'.format(self.balance)}. {'${:,.2f}'.format(amount)} is over your limit.")

    def calc_interest(self): 
        print(f"Your interest on the year will be {'${:,.2f}'.format(self.balance * self.interest)}.")

    def print_transactions(self):
        print("Your transaction history: ")
        for transaction in self.transactions:
            print("\t",transaction)

    def quit(self):
        self.cont = "n"

    def run(self):
        print(f"Welcome to Trustworthy Bank, {self.name}. Where you can trust us because you don't have a choice. ")
        actions = ["Check balance, Check history, Check interest, Deposit, Withdraw, Quit"]
        #this part matches a text input with a function to later call. 
        functions = {"check balance": self.check_balance,"check history": self.print_transactions,"check interest": self.calc_interest,"deposit": self.deposit,"withdraw": self.withdraw,"quit": self.quit}
        while self.cont == "y":
            print("\nWhat would you like to do? (Check balance, Check history, Check interest, Deposit, Withdraw, or 'Quit' to exit.)")
            action = helper.text_checker(input("> "),actions)
            functions[action]()


    

if __name__ == "__main__":
    print("Please enter a name to create an account: ")
    name = input("> ")
    new_account = ATM(name)
    new_account.run()

