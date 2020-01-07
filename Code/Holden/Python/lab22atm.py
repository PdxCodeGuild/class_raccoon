import re
from decimal import Decimal

class atm:
    def __init__(self, bal = 0, intrst = 0.1):
        self.bal = bal
        self.intrst = intrst
        self.history = []

    def check_balance(self):
        return "$" + str(self.bal)

    def print_history(self):
        for transaction in self.history:
            print(transaction)

    def deposit(self, amount):
        self.bal += amount
        print(f"${amount} has been deposited to account.")
        self.history.append(f"User deposited ${amount}")

    def check_withdrawl(self, amount):
        return self.bal - amount > 0

    def withdrawl(self, amount):
        if check_withdrawl(amount):
            self.bal -= amount
            print(f"${amount} has been withdrawn from account.")
            self.history.append(f"User withdrew ${amount}")
        else:
            print("We kept you from overdrawing your account because we're nice people.")
            print(f"You have ${self.bal} in your account.")

    def calc_interest(self):
        return round(Decimal(self.bal * self.intrst),2)

def clean_input(usin):
    found_d_smb = usin.find("$")
    found_dol = usin.find("dollars")
    found_cents = usin.find("cents")
    dollars = 0
    cents = 0
    if found_dol != -1 and found_d_smb != -1:
        return None
    if found_dol + found_d_smb !=-2 and found_cents != -1:
        if len(re.findall(r"\d+", usin)) < 2:
            return None
        if re.search(r"\d+\.?\d* ?dollars", usin) == None or re.search(r"\d+ ?cents", usin) == None:
            return None
        if re.search(r"\$\d+\.*\d* ?cents", usin):
            return None
    if found_cents != -1:
        cents_value = re.findall(r"(\d+).?cents", usin)
        if len(cents_value) != 1:
            return None
        cents += Decimal(int(cents_value[0])/100)
    if found_dol != -1:
        dollar_value = re.findall(r"(\d+)\.*\d* ?dollars", usin)
        if len(dollar_value) != 1:
            return None
        dollars = Decimal(dollar_value[0])
        dollar_cents = re.findall(r"\d+\.*(\d{2}) ?dollars", usin)
        if len(dollars_cents) == 1 and dollar_cents[0]:
            cents += Decimal("0." + dollar_cents[0])
    if found_d_smb != -1:
        dollar_value = re.findall(r"\$(\d+)\.*\d*", usin)
        if len(dollar_value) != 1:
            return None
        dollars = Decimal(dollar_value[0])
        dollar_cents = re.findall(r"\$\d+\.*(\d{2})", usin)
        if len(dollar_cents) == 1 and dollar_cents[0]:
            cents += Decimal("0." + dollar_cents[0])
    if dollars + cents != 0:
        return round(Decimal(dollars + cents),2)

validin = ["deposit", "depo", "withdraw", "with", "check balance", "check", "history", "hist"]
quitprompt = ["quit", "q", "exit"]
deposit_prompt = ["deposit", "depo"]
withdraw_prompt = ["withdraw", "with"]
check_prompt = ["check balance", "check"]
history_prompt = ["history", "hist"]
user = atm(0, 0.1)
while True:
    usin = input("> what would you like to do (deposit, withdraw, check balance, history, quit)? \n> ").lower()
    if usin in quitprompt:
        break
    if usin not in validin:
        print("invalid input")
        continue
    if usin in deposit_prompt:
        cleaned = None
        while cleaned == None:
            usin = input("Input deposit amount: \n> ")
            cleaned = clean_input(usin)
            if cleaned == None:
                print("Please input a valid dollar amount")
        user.deposit(cleaned)
    if usin in withdraw_prompt:
        cleaned = None
        while cleaned == None:
            usin = input("Input withdrawl amount: \n> ")
            cleaned = clean_input(usin)
            if cleaned == None:
                print("Please input a valid dollar amount")
        user.withdrawl(cleaned)
    if usin in check_prompt:
        print(f"Your balance is {user.check_balance()}")
    if usin in history_prompt:
        user.print_history()
