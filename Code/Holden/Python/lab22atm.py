import re


class atm:
    def __init__(self, bal = 0, intrst = 0.1):
        self.bal = bal
        self.intrst = intrst
        self.history = []

    def check_balance():
        return self.bal

    def deposit(amount):
        self.bal += amount
        print(f"${amount} has been deposited to account.")
        self.history.append(f"User deposited ${amount}")

    def check_withdrawl(amount):
        return self.bal - amount > 0

    def withdrawl(amount):
        if check_withdrawl(amount):
            self.bal -= amount
            print(f"${amount} has been withdrawn from account.")
            self.history.append(f"User withdrew ${amount}")
        else:
            print("We kept you from overdrawing your account because we're nice people.")
            print(f"You have ${self.bal} in your account.")

    def calc_interest():
        return decimal(self.bal * self.intrst)

def clean_input(usin):
    found_d_smb = usin.find("$")
    found_dol = usin.find("dollars")
    found_cents = usin.find("cents")
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
        # need to fix search thingy
        cents += int("0." + re.findall(r"(\d).?cents", usin))
    if found_dol != -1:
        dollars = int(re.search(r"(\d+)\.*\d* ?dollars", usin))
        if re.search(r"\d+\.*(\d*) ?dollars", usin):
            cents += int("0." + re.search(r"\d+\.*(\d*) ?dollars", usin))
    if found_d_smb != -1:
        dollars = int(re.search(r"(\d+)\.*\d*", usin))
        if re.search(r"\$\d+\.*(\d*)", usin):
            cents += int("0." + re.search(r"\$\d+\.*(\d*)", usin))
    if dollars + cents != 0:
        return decimal(dollars + cents)

validin = ["deposit", "depo", "withdraw", "with", "check balance", "check", "history", "hist"]
quitprompt = ["quit", "q", "exit"]
deposit_prompt = ["deposit", "depo"]
user = atm(0, 0.1)
while True:
    usin = input("> what would you like to do (deposit, withdraw, check balance, history)? \n> ").lower()
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
