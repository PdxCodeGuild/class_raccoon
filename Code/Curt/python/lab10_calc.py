#lab10_calc.py
oper_list = ["+","-","*","/"]
oper = ""

while oper not in oper_list: #get operation type
    oper = input("What operation would you like to perform (+, -, *, or /)? ")

again = True
while again == True:
    #get numbers to calculate
    num1 = ""
    while isinstance(num1, float) == False:
        num1 = input("What is the first number? ")
        try:
            num1 = float(num1)
        except ValueError:
            print("Invalid entry!")

    num2 = ""
    while isinstance(num2, float) == False:
        num2 = input("What is the second number? ")
        try:
            num2 = float(num2)
        except ValueError:
            print("Invalid entry!")

    #output results
    if oper == "+":
        total = num1 + num2
        print(f"{num1} + {num2} = {total}")
    elif oper == "-":
        total = num1 - num2
        print(f"{num1} - {num2} = {total}")
    elif oper == "*":
        total = num1 * num2
        print(f"{num1} * {num2} = {total}")
    else:
        try:
            total = num1 / num2
            print(f"{num1} / {num2} = {total}\n")
        except ZeroDivisionError:
            print("Error! Cannot divide by zero!")

    #Version 2: Go again
    oper = ""
    while oper not in oper_list: #get operation type
        oper = input("Do another operation (+, -, *, or /), or type 'done' to quit: ").casefold()
        if oper == "done":
            again = False
            break
        else:
            again = True

print("Goodbye!")
