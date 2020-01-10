
class Battle_Roll:

# Begins functions inside class
    def __init__(self):
        self.hp = 100
        print(f"HP Status: {self.hp}")

    def check_hp(self):
        print(self.hp)

    # def deposit(self):
    #     amount = float(input('How much do you want to deposit? '))
    #     self.hp += amount
    #     print('Amount deposited:', amount)

# start and call ATM class
start = Battle_Roll()
# start.check_hp()
# start.deposit()
print()
