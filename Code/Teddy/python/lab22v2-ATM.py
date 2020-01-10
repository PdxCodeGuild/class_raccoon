'''
Lab 22: ATM
Version 2

Have the ATM maintain a list of transactions.
Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'.
Add a new function print_transactions() to your class for printing out the list of transactions.
'''
# ATM class
class Atm:
    # self initial function
    def __init__(self, bal=0, rate=0.001):
        self.bal = bal
        self.rate = rate
        print('Welcome to your ATM account!')

    # Checking balance function
    def check_balance(self):
        # returns the account balance
        return (f'Your current balance: ${self.bal}')

    # Deposit function that given amount in the account
    def deposit(self, amount):
        self.bal += amount

    # Checking withdraw function
    def check_withdrawal(self, amount):
        # Check if there is enough money to withdraw in account
        if self.bal >= amount:
            # returns true if the withdrawn amount won't put the account in the negative
            return True
        else:
            # if not, return false
            return False

    # withdraw function
    def withdraw(self, amount):
        self.bal -= amount

    # calculate balance function
    def calc_interest(self):
        # returns the amount of interest calculated on the account
        return self.bal * self.rate

    # print transection
    def print_transactions(self):
        return self.check_balance()

print(f'-'* 80)
atm = Atm()
print(f'-'* 80)

atm = Atm()
while True:
    # user's input options Deposit, Withdraw, Balance or Quit
    user_input = input('Deposit, Withdraw, Balance, Quit: ').lower()
    # if deposit
    if user_input == 'deposit':
        # user input amount of deposit
        amount_deposit = float(input(f'Enter the deposit amount: $'))
        # call function deposit
        atm.deposit(amount_deposit)
        # Output message
        print(f'User deposit: ${amount_deposit}')
    # if withdraw
    elif user_input == 'withdraw':
        # withdraw
        amount_withdraw = float(input(f'Enter the withdraw amount: $'))
        # Condition check that the user have enough money to withdraw or not
        can_withdraw = atm.check_withdrawal(amount_withdraw)
        # If enough money
        if can_withdraw:
            # call function withdraw
            atm.withdraw(amount_withdraw)
            # Output message
            print(f'User withdraw: ${amount_withdraw}')
        # if not enough money
        else:
            # Output message
            print(f'You don\'t have enough money to withdraw')
    # if user want to check balance
    elif user_input == 'balance':
        # call function print_transactions
        print(atm.print_transactions())
    # if user want to quit
    elif user_input == 'quit':
        # Output message
        print('Bye')
        print()
        # Break out of the program
        break
    # the user input not in the option
    else:
        # Output message ('Deposit, Withdraw, Balance, Quit')
        print('Invalid input')
    print()
