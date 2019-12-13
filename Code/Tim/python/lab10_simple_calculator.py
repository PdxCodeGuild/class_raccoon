num1 = int(input("What is your first number? "))
num2 = int(input("What is your second number? "))
operation = input("What would you like to do to these two numbers? (+,-,*,/) ")
if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
else:
    print(num1 / num2)
