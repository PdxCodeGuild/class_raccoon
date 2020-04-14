'''
Lab 22: ATM

Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account
'''
import math



class AtmAccount:
    def __init__(self, username, password, balance, transactions = []):
        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = transactions

    def check_credentials(self, username, password):
        return self.username == username and self.password == password


class Atm:
    def __init__(self, interest=0.001):
        self.interest = interest
        self.accounts = [
            AtmAccount('alex', 'alex', 100),
        ]
        self.current_account = None

    def login(self, username, password):
        for account in self.accounts:
            if account.check_credentials(username, password):
                self.current_account = account
                print('logged in as ' + self.current_account.username)
                break
        else:
            print('could not find a user with that username and password')

    def logout(self):
        self.current_account = None

    def deposit(self, amount):
        if self.current_account is None:
            print('not logged in')
            return None
        self.current_account.balance += amount
        self.__round()
        self.current_account.transactions.append(f"{self.current_account.username} deposited $%.2f." %amount) #adds entry to transaction history
        print("$%.2f deposited." %amount)
        print("Your new balance is $%.2f." %self.current_account.balance)

    def check_withdrawal(self, amount):
        return amount <= self.current_account.balance

    def withdraw(self, amount):
        if self.current_account is None:
            print('not logged in')
            return None
        if self.check_withdrawal(amount): #tests for sufficient funds
            self.current_account.balance -= amount
            self.__round()
            self.current_account.transactions.append("User withdrew $%.2f." %amount) #adds entry to transaction history
            print("$%.2f withdrawn." %amount)
            print("Your new balance is $%.2f." %self.current_account.balance)
        else:
            print("Insufficient funds! Your current balance is $%.2f." %self.current_account.balance)

    #function for calculating interest rate
    def calc_interest(self):
        return round(self.current_account.balance * self.interest, 2)

    #function for displaying list of transactions
    def display_transactions(self):
        print(*self.current_account.transactions, sep = '\n')

    #restricts all inputs to two decimal places
    def __round(self):
        self.current_account.balance = round(self.current_account.balance, 2)

    def balance(self):
        if self.current_account is None:
            print('not logged in')
            return None
        return self.current_account.balance


atm = Atm()
userinput = ''

while userinput != 'quit':
    while True:
        command = input('what would you like to do? (login, logout, deposit, withdraw, balance, history or quit) ')
        if command == 'login':
            username = input('what is your username? ')
            password = input('what is your password? ')
            atm.login(username, password)
        elif command == 'logout':
            atm.logout()
        elif command == 'deposit':
            amount = float(input('what is the amount? $'))
            atm.deposit(amount)
        elif command == 'withdraw':
            amount = float(input('what is the amount? $'))
            atm.withdraw(amount)
        elif command == 'balance':
            print(f'\n\n${atm.balance()}\n\n')
        elif command == 'history':
            print("Here's your list of transactions:")
            atm.display_transactions()
        else:
            print('command not recognized')