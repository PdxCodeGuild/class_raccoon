# Lab 10: Simple Calculator

# Additional function
def Add(num1, num2):
    return num1 + num2

# Subtraction function
def Sub(num1, num2):
    return num1 - num2

# Muliplication function
def Mul(num1, num2):
    return num1 * num2

# Division function
def Div(num1, num2):
    return num1 / num2

def print4(x):
    return(round(x,4))


valid_operators = ['+', '-', '*', '/']
play_again = 'y'

while play_again == 'y':
    operator = input('What is the operation you\'d like to perform?(+, -, *, /)')

    if operator not in valid_operators:
        print('Invalid operator')
        continue

    first_number = int(input('What is the first number? '))
    second_number = int(input('What is the second number? '))
    if operator == '+':
        print(f'{first_number} {operator} {second_number} is {print4(Add(first_number, second_number))}')

    elif operator == '-':
        print(f'{first_number} {operator} {second_number} is {print4(Sub(first_number, second_number))}')

    elif operator == '*':
        print(f'{first_number} {operator} {second_number} is {print4(Mul(first_number, second_number))}')

    elif operator == '/':
        print(f'{first_number} {operator} {second_number} is {print4(Div(first_number, second_number))}')
    else:
        print('Invalid operator')

    play_again = input('Do you want to perform again?(y/n)').lower()

else:
    print('Bye!')
