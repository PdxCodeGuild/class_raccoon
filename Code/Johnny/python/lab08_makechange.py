# lab08_makechange.py

# dictionary of coins key/value
coins = {'quarter' : 25, 'dime' : 10, 'nickel' : 5, 'penny' : 1}

# user input and prompt for change type.
print("Let's make change.")
user_var = int(input("Enter a number: "))
user_curr = input("Quarter, Dime, Nickel or Penny: ").lower().strip()
output = user_var//coins[f'{user_curr}']
print(f"Your {user_var} changes to {output} {user_curr}.")
