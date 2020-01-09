
import os
from decimal import Decimal

class Dollars:
    def __init__ (self, balance):
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += float(amount)

    def check_withdrawal(self, amount):
        if self.balance <= float(amount):
            print('Not enough funds. ')

        else:
            self.withdraw()

    def withdraw(self, amount):
        self.balance -= float(amount)

    def calc_interest(self):
        time = int(input('How many months do we have your money? '))
        apy = self.balance * (1.001 ** (time - 1))
        print(apy)

def TBT_header():
    os.system('cls')
    print('*****************************************************')
    print('*********-----TimBank and Trust ATM-----*************')
    print('*****************************************************')



user = Dollars(100)

while True:
    TBT_header()
    userchoice = input('\n\nWhat would you like to do with your money?\n(C)heck Balance, (D)eposit Money, \n(W)ithdraw Money, (Ca)lculate Interest\n>\n\n*****************************************************\n*****************************************************').lower()

    if userchoice == 'c': #CHECK BALANCE
        TBT_header()
        print(f'\n\n\nYour new balance is ${user.balance}.\n\n\n*****************************************************\n*****************************************************')
        break
    elif userchoice == 'd': #DEPOSIT
        TBT_header()
        dep_amount = float(input('\n\n\nHow much would you like to deposit?\n>\n\n\n*****************************************************\n*****************************************************'))
        user.deposit(dep_amount)
        TBT_header()
        print(f'\n\n\nYour new balance is ${user.balance}.\n\n\n*****************************************************\n*****************************************************')
        break
    elif userchoice == 'w': #WITHDRAW
        TBT_header()
        with_amount = float(input('\n\n\nHow much would you like to withdraw?\n>\n\n\n*****************************************************\n*****************************************************'))
        user.check_withdrawal(with_amount)
        user.withdraw(with_amount)

        TBT_header()
        print(f'\n\n\nYour new balance is ${user.balance}.\n\n\n*****************************************************\n*****************************************************')
        break
    elif userchoice == 'ca': #CALCULATE INTEREST
        TBT_header()
        user.calc_interest()
        print(user.balance)
        print(apy)
