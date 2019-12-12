import string
coinage={25:"quarters", 10:"dimes", 5:"nickels", 1:"pennies"}
punc=string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.whitespace
while True:
    cash=input("Please input the amount of cash(either in pennies or $1.00 format): ")
    cash="".join(char for char in cash if char not in punc)
    if not cash.isdigit():
        print("Please input a valid number.")
        continue
    cash=int(cash)
    output="You have"
    for coin in coinage:
        output+=" "+str(cash//coin)+" "+str({coinage[coin]})
        cash = cash%coin
    print(output+".")
    break
