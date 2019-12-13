
coins = [
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

amount = input('Please enter a dollar amount $')
amount = int(float(amount)*100)

for coin in coins:
    num_coins = amount//coin[1]
    print(f'{num_coins} {coin[0]}')
    # print(amount)
    # print(coin[1])
    amount %= coin[1]
    # print(amount)
    # print()
    # amount -= coin[1]*num_coins
