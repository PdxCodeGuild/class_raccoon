import math

# default to a balance of 0 and an interest rate of 0.1%. Implement the initializer

class ATM:
    def __init__(self, balance = 0, int_rate = 0.01, activity = []):
        self.balance = balance
        self.int_rate = int_rate
        self.activity = activity

#check activity

    def check_activity(self):
        return self.activity

# check_balance() returns the account balance

    def check_bal(self):
        return self.balance       

# deposit(amount) deposits the given amount in the account

    def deposit(self, add):
        self.balance += add
        self.activity.append(f"User deposited ${add}")

# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative

    def check_with(self, check):
        if self.balance - int(check) > 0:
            return True

# withdraw(amount) withdraws the amount from the account and returns it

    def withdraw(self, withdrawl):
        self.balance -= withdrawl
        self.activity.append(f"User withdrew ${withdrawl}")
# calc_interest() returns the amount of interest calculated on the account 
    
    def check_int(self):
        return self.balance * self.int_rate


#actuall ATM part
choice = ""

balance = 0
atm = ATM(balance)
while True:

    choice =  input("\n Would you like to check your balance, make a deposit, make a withdrawl, see your recent activity, order chicken, or quit?\n").lower()

    if "check" in choice:
        print("Your balance is", atm.check_bal())
    
    elif "deposit" in choice:
        dpt = int(input("How much would you like to deposit? "))
        dpt_check = input(f"You would like to deposite ${dpt} Y/N? ").lower()
        if dpt_check == "y":
            atm.deposit(dpt)
            print(f"Your new balance is ${atm.check_bal()}.")
        else:
            continue
    elif "withdraw" in choice:
        with_req = int(input("How much would you like to withdraw? "))
        yes_no = atm.check_with(with_req)
        if yes_no == True:
            atm.withdraw(with_req)
            print(f"Your current balance is ${atm.check_bal()}")
        else:
            print("Insufficient funds")
            continue
    elif "quit" in choice:
        int_total = atm.check_int()
        atm.deposit(int_total)
        print(f"\nThanks for banking with ShadyBank, the shadiest bank in town! Your balance with interest is {atm.check_bal()}\n")
        break
    elif "activity" in choice:
        print(atm.check_activity())
    elif "chicken" in choice:
        print("\nThis is a bank, why would we have chicken for sale?\n")
    else:
        print("\nInvalid selection, please try again.\n")
        continue