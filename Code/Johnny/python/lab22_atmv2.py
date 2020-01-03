
# ATM CLASS will call this section by name 'Member_Account'
class Member_Account:

# Begins functions inside class
    def __init__(self):
        self.balance = 0
        self.transaction = []
        print("Welcome to Bank of Portototolando. ")

    def check_balance(self):
        print('$', self.balance)

    def deposit(self):
        amount = float(input('How much do you want to deposit? '))
        self.balance += amount
        self.transaction.append(f'Deposited ${amount}') #append to list above
        print('Amount deposited: $', amount)

    def check_withdrawal(self):
        amount_out = float(input('How much do you want to withdraw? '))
        if self.balance >= amount_out:
            self.balance -= amount_out
            self.transaction.append(f'Withdraw ${amount_out}')
            print('Withdraw amount: $', amount_out)
        else:
            print('Fund Error.')

    def calc_interest(self):
        interest = self.balance * .01
        print('Interest at .1%, Gained: $', interest)

    def print_trans(self):
        print(self.transaction)

# start and call ATM class and each functions
start = Member_Account()
start.deposit()
start.check_withdrawal()
start.calc_interest()
start.check_balance()
start.print_trans()
