#calculate user inputs
#different opperations
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

#getting user input, I'm going to make this smarter at some point
operation = input("What kind of operation would you like? (+,-,*,/) ")
num1 = float(input("Choose the first number "))
num2 = float(input("Now choose the second number"))

#logic to decide which function to call
if operation == "+":
    print(f"{num1} + {num2} = ", add(num1, num2))
elif operation == "-":
    print(f"{num1} - {num2} = ", sub(num1, num2))
elif operation == "*":
    print(f"{num1} * {num2} = ", mult(num1, num2))
elif operation == "/":
    print(f"{num1} / {num2} = ", div(num1, num2))
else:
    print("Invalid input")