



class AtmAccount:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance

    def check_credentials(self, username, password):
        return self.username == username and self.password == password


class Atm:
    def __init__(self, interest=0.001):
        self.interest = interest
        self.accounts = [
            AtmAccount('joe', 'joespassword123', 50),
            AtmAccount('jill', 'jillspassword', 75)
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

    def withdraw(self, amount):
        if self.current_account is None:
            print('not logged in')
            return None
        self.current_account.balance -= amount

    def balance(self):
        if self.current_account is None:
            print('not logged in')
            return None
        return self.current_account.balance




atm = Atm()

while True:
    command = input('what would you like to do? (login, logout, deposit, withdraw, balance) ')
    if command == 'login':
        username = input('what is your username? ')
        password = input('what is your password? ')
        atm.login(username, password)
    elif command == 'logout':
        atm.logout()
    elif command == 'deposit':
        amount = float(input('what is the amount? '))
        atm.deposit(amount)
    elif command == 'withdraw':
        amount = float(input('what is the amount? '))
        atm.withdraw(amount)
    elif command == 'balance':
        print(atm.balance())
    else:
        print('command not recognized')






