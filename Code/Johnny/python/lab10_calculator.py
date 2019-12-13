# lab10_calculator.py

equation = input("Whats the equation, (3 + 5): ").split(" ")
num1 = float(equation[0])
operate1 = equation[1]
num2 = float(equation[2])

if equation[1] == '+':
    print(num1 + num2)
elif equation[1] == '-':
    print(num1 - num2)
elif equation[1] == '*':
    print(num1 * num2)
elif equation[1] == '/':
    print(num1 / num2)
else:
    print("Invalid choice. ")
