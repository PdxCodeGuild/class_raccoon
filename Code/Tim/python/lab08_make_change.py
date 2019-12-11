import os

os.system('cls')

input = float(input("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\nHow much money do you have in decimals? (e.g. 999.72)\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n> "))
input = input * 100

dollars = 100
quarters = 25
dimes = 10
nickels = 5

dollarback = input // dollars
input = input % dollars
quarterback = input // quarters
input = input % quarters
# input = round(input,2)
dimesback = input // dimes
input = input % dimes
# input = round(input,2)
nickelsback = input // nickels
input = input % nickels
# input = round(input,2)

print(f"You get {dollarback} dollars, {quarterback} quarters, {dimesback} dimes, {nickelsback} nickels, and {input} pennies. ")
