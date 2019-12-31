'''
Lab 10: Simple Calculator

Version 2

Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!
'''


print("I am a simple calculator.\n\n\n")

calculation = input("What is the operation you would like to perform?\n\nEx.) 1 + 1\n\n")

calculation = calculation.split(' ')

operand1 = int(float(calculation[0]))

operation = calculation[1]

operand2 = int(float(calculation[2]))

while True:


    if operation == '+':
        print(f"{operand1} {operation} {operand2} = {operand1 + operand2}\n")

    elif operation == '-':
        print(f"{operand1} {operation} {operand2} = {operand1 - operand2}\n")

    elif operation == '*':
        print(f"{operand1} {operation} {operand2} = {operand1 * operand2}\n")

    elif operation == '/':
        print(f"{operand1} {operation} {operand2} = {operand1 / operand2}\n")

    if_done = input("If you are done type 'done'\n\n")

    if if_done == 'done':
        break
