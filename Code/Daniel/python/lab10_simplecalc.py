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
equation = input("Input equation with spaces: ").split(" ")
num1 = int(equation[0])
num2 = int(equation[2])
operation = equation[1]

# logic to decide which function to call
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