#Calculator lab
import operator


cont_list = ["Yes", "yes", "continue"]

#Operator module will take the input and perform the calculation
def calculate(op,op1,op2):
    operators  = {
    "+": operator.add(op1,op2),
    "-": operator.sub(op1,op2),
    "*": operator.mul(op1,op2),
    "/": operator.floordiv(op1,op2),
}
    return operators.get(op)


print("Welcome to the calculator.......")
#Main program section with while loop
while True:
    user_calculate = input("Enter your equation i.e (5 + 2). Make sure to put a space between numbers. \n:")
    user_calculate = user_calculate.split(' ')
    operand_1 = int(user_calculate[0])
    op = user_calculate[1]
    operand_2 = int(user_calculate[2])

    print(f"{operand_1}{op}{operand_2} = {calculate(op, operand_1, operand_2)}")
    again = input("Do you have another calculation?")
    if again in cont_list:
        continue
    else:
        print("Goodbye")
        break

