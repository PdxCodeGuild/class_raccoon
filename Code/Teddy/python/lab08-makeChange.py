# Lab 8: Make Change

# Setup dictionary
coins = {
  "quarter": 25,
  "dime": 10,
  "nickle": 5,
  "penny": 1
}

change_again = 'y'

while change_again == 'y':
    # User prompt in pennies
    pennies = int(input('How many pennies do you have? '))

    # Converse the pennies to quarters
    quarters = pennies // coins['quarter']

    # The pennies leftover after quarters
    pennies_quarters = pennies % coins['quarter']

    # Converse the pennies leftover after quarters to dimes
    dimes = pennies_quarters // coins['dime']

    # The pennies leftover after dimes
    pennies_dimes = pennies_quarters % coins['dime']

    # Converse the pennies leftover after dimes to nickles
    nickles = pennies_dimes // coins['nickle']

    # The pennies leftover after nickles
    pennies_nickles = pennies_dimes % coins['nickle']


    print(f'You have {quarters} quarters, {dimes} dimes, {nickles} nickles and {pennies_nickles} pennies')

    change_again = input('Do you want to change again? (y/n)').lower()

else:
    print('See you again!')
