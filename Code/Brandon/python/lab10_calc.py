#Calculator lab
import operator


#dictionary of operators
operators  = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,

}


# def calculate(num1,oper,num2):
#     break





print("Welcome to the calculator. Cant believe you need me for basic calculations.......")

user_calculate = input("Enter your equation i.e (5+2) \n:")
user_calculate = user_calculate.split
print(user_calculate)



operand_1 = user_calculate[1]
operator = user_calculate[2]
operand_2 = user_calculate[3]

# print(operand_1)

# if operand_2 == int:
#     print (operand_2)
# if operand_2 == int:
#     print (operand_1)
# # print(operator)


# operand_1 = input("What is the first number?\n:")
# operand_1 = float(operand_1)

# operator = input("What is the operator?\n:")
# operator_converted = operators[operator]

# operand_2 = input("What is the second number?")
# operand_2 = float(operand_2)


# text = input('Enter your conversion (5 miles in inches): ')
# text = text.split(' ')
# distance = text[0]
# input_units = text[1]
# output_units = text[3]


# calculate(operand_1,operator,operand_2)