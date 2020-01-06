# lab08_makechange.py

# dictionary of coins key/value
coins = {'quarter' : 25, 'dime' : 10, 'nickel' : 5, 'penny' : 1}

# user input and prompt
user_var = float(input("Enter a dollar amount '1.57': "))
output = user_var*100
print(f"Your {user_var} changes to {output} pennies.")
