#lab22_atm.py
import math

class ATM:
    def __init__(self, balance = 0, interest = 0.001, transactions = []):
        self.balance = round(balance, 2)
        self.interest = interest
        self.transactions = transactions

    def check_balance(self):
        self.__round()
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.__round()
        self.transactions.append("User deposited $%.2f." %amount)
        print("$%.2f deposited." %amount)
        print("Your new balance is $%.2f." %self.balance)


    def check_withdrawal(self, amount):
        return amount <= self.balance

    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.balance -= amount
            self.__round()
            self.transactions.append("User withdrew $%.2f." %amount)
            print("$%.2f withdrawn." %amount)
            print("Your new balance is $%.2f." %self.balance)
        else:
            print("Insufficient funds! Your current balance is $%.2f." %self.balance)

    def calc_interest(self):
        return round(self.balance * self.interest, 2)

    def print_transactions(self):
        print(*self.transactions, sep = '\n')

    def __round(self):
        self.balance = round(self.balance, 2)

balance = float(input('What is your starting balance? '))
balance = ATM(balance)
print("Your current balance is $%.2f." %balance.check_balance())
print("Your accrued interest on $%.2f is $" %balance.check_balance() + "%.2f" %balance.calc_interest())

#VERSION 3 - REPL
replist = ('deposit', 'withdraw', 'check balance', 'history','quit')

userinput = ''
while userinput != 'quit':
    while True:
        userinput = input("What would you like to do (deposit, withdraw, check balance, history, quit)? ").casefold()
        if userinput in replist:
            break
        else:
            print("Invalid entry!")

    if userinput == 'deposit':
        deposit = round(float(input("How much would you like to deposit? ")), 2)
        balance.deposit(deposit)

    elif userinput == 'withdraw':
        withdraw = round(float(input("How much would you like to withdraw? ")), 2)
        balance.withdraw(withdraw)

    elif userinput == 'check balance':
        print("Your current balance is $%.2f" %balance.check_balance())

    elif userinput == 'history':
        print("Here's your list of transactions:")
        balance.print_transactions()

    else:
        break