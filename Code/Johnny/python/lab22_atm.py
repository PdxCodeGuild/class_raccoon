
# ATM CLASS will call this section by name 'Member_Account'
class Member_Account:

# Begins functions inside class
    def __init__(self):
        self.balance = 0
        print("Welcome to Bank of Portototolando. ")

    def check_balance(self):
        print(self.balance)

    def deposit(self):
        amount = float(input('How much do you want to deposit? '))
        self.balance += amount
        print('Amount deposited:', amount)

    def check_withdrawal(self):
        amount_out = float(input('How much do you want to withdraw? '))
        if self.balance >= amount_out:
            self.balance -= amount_out
            print('Withdraw amount', amount_out)
        else:
            print('Fund Error.')

    def calc_interest(self):
        interest = self.balance * .10
        print('Interest calculated at rate of .10%')
        print('Gained:', interest)

# start and call ATM class
start = Member_Account()
start.check_balance()
start.deposit()
start.check_withdrawal()
start.calc_interest()
