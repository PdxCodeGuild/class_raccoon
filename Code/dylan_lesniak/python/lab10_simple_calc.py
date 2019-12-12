'''
Filename: lab10_simple_calc.py
Author: Dylan
Purpose: Create simple REPL calculator
'''

#do I want to make it able to handle things like parentheses? 
#If so, I have to write in rules, right? 

def calc():
    print("Welcome to calculator")
    print("Please enter your first number: ")
    first_num = digit_checker(input("> "))
    print("Please enter desired operation: (+ - * /)")
    operation = oper_checker(input("> "))
    print("Please enter your second number: ")
    second_num = digit_checker(input("> "))
    answer = do_math(first_num,second_num,operation)
    print(f"Your answer is: {answer}")

def do_math(num1,num2,oper):
    num1 = int(num1)
    num2 = int(num2)
    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2
    elif oper == "/":
        return num1 / num2
    print("You shouldn't have gotten here. Line 32")

def digit_checker(num):
    while True:
        if num.isdigit():
            return num
        else:
            print("Please enter valid integer: ")
            num = input("> ")

def oper_checker(oper):
    opers = "+-*/"
    while True:
        if oper in opers:
            return oper
        else: 
            print("Please enter valid operation: (+ - * /)")
            oper = input("> ")

cont = 'y'
while cont == 'y':
    calc()
    print("Would you like to calculate something else? (y/n)")
    cont = input("> ").lower()