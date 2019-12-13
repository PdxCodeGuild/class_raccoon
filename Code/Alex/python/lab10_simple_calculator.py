'''
Lab 10: Simple Calculator

Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.

> What is the operation you'd like to perform? +
> What is the first number? 5
> What is the second number? 12
> 5 + 12 = 17
'''


print("I am a simple calculator.\n\n")

operation = (input("What is the operation you would like to perform? "))

operator = float(int(input("\nWhat is the operator (first number in the equation)? ")))

operand = float(int(input("\nWhat is the operand or the quantity on which an operation is to be done? ")))

calculation = (operator) + (operation) + (operand)

print(calculation)
