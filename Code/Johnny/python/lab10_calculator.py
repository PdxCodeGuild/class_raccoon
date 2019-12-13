# lab10_calculator.py

user_input = input("Please enter a number (1 - 4) : \n"
    "1. Add \n"
    "2. Subtract \n"
    "3. Multiply \n"
    "4. Divide \n")
user_input1 = int(input("What's the first number: "))
user_input2 = int(input("What's the second number: "))

if user_input == '1':
    results = user_input1 + user_input2
    print(results)
elif user_input == '2':
    results = user_input1 - user_input2
    print(results)
elif user_input == '3':
    results = user_input1 * user_input2
    print(results)
elif user_input == '4':
    results = user_input1 / user_input2
    print(results)
else:
    print("Invalid choice. ")
