# lab08_makechange
# enter a number and convert it to a useable int
user_coins = input('Enter a number to change? >> ')
user_coins = float(user_coins) * 100
user_coins = int(user_coins)
# floor divide, mods and break coins into smaller
q = user_coins // 25
remain = user_coins % 25
dimes = remain // 10
remain = remain % 10
nickles = remain // 5
remain = remain % 5
penny = remain // 1
# break down the number into smaller coins and rid of remainder lots more quarters
print(f"Your coins {user_coins}: \nQuarters  >>{q} \nDimes   >>{dimes} \nNickles  >>{nickles}  \nPennies  >>{penny}")
