'''
Lab 22: ATM

Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account
'''


import os
import string


class Atm:
    def balance(self):
        return self.current_account.balance

    def deposit(self, amount):
        self.current_account.balance += amount #deposits the given amount in the account


    def check_withdrawal(self, amount) #returns true if the withdrawn amount won't put the account in the negative


    def withdraw(self, amount):
        self.current_account.balance -= amount #withdraws the amount from the account and returns it


    def calc_interest(self, interest=0.001):
        self.interest = interest






#implement teller or self serve
atm = Atm()

while True:
    os.system("clear")
    pin = input("ATM\n\nPIN: ")

    if not pin.isdigit() or len(pin) != 4:
            print("Invalid PIN")
            break

    else:
        account = input("\n\nOptions:\nSavings\nChecking\n\n").lower()
        if account == "savings":

            duty = input('\n\nOptions:\nCheck balance\nWithdraw\nDeposit\nCancel\n\n').lower()

            if duty == 'balance':
                print(f"Your current balance in your {account} account is ${}")

            elif duty == 'withdraw':
                amount = input('Please enter the amount you would like to withdraw\n$')

            elif duty == 'deposit':
                amount = input('Please enter the amount you would like to deposit\n$')

            elif duty == 'cancel':
                cancel = input('Cancel transaction? ')
                if cancel == "yes" or "y":
                    print("Goodbye!")
                else:
                    break
            else:
                print('invalid entry')
                input()

        if account == "checking":
            duty = input('\n\nOptions:\nCheck balance\nWithdraw\nDeposit\nCancel\n\n').lower()

            if duty == 'balance':
                print(f"Your current balance in your {account} account is ${}")

            elif duty == 'withdraw':
                amount = input('Please enter the amount you would like to withdraw\n$')

            elif duty == 'deposit':
                amount = input('Please enter the amount you would like to deposit\n$')

            elif duty == 'cancel':
                cancel = input('Cancel transaction? ')
                if cancel == "yes" or "y":
                    print("Goodbye!")
                else:
                    break
            else:
                print('invalid entry')
                input()

        else:
            print('invalid entry')
            input()