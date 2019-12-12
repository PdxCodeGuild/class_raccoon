#Make Change, Brandon G.

coins = {"quarter": 25,"dime": 10,"nickel": 5,"penny": 1}



def my_change(money):
    money = money * 100
    money = int(money)

    quarters = money // coins["quarter"]

    money = money % coins["quarter"]

    dimes = money // coins["dime"]

    money = money % coins["dime"]

    nickels = money // coins["nickel"]

    
    pennies = money

    print(f" You have {quarters} quarters, {dimes} dimes, {nickels} nickles, and {pennies} pennies")

while True:
    print("Welcome to the change program.")

    user_money = input("Enter your dollar amount. i.e '1.35'\n:")
    user_money = float(user_money)

    my_change(user_money)

    tryagain = input("Again? Yes or no : ")

    if tryagain == "no":
        print("Goodbye")
        break
