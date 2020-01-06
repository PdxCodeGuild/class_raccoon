#Purpose: To create a program using the by-hand version of arithmetic
#sorry

first_num = []
second_num = []

while True:

    num1 = input("What is the first number you would like to add? ")
    num2 = input("What is the second number you would like to add? ")

    if num1.isdigit() and num2.isdigit():
        break
    else:
        print("INVALID INPUTS!!!")

num1 = list(num1)
num2 = list(num2)

num1.reverse()
num2.reverse()
num1 = [int(x) for x in num1]
num2 = [int(x) for x in num2]

def equal_lengths(num1,num2):
    if len(num1) > len(num2):
        for i in range(len(num1)-len(num2)):
            num2.append(0)
    elif len(num1) < len(num2):
        for i in range(len(num2)-len(num1)):
            num1.append(0)


def addition(num1, num2):
    equal_lengths(num1,num2)
    carry = 0
    output = []
    for i in range(len(num1)):
        current_digit = carry + num1[i] + num2[i]
        # print(num1,num2,current_digit)
        carry = current_digit // 10
        output.append(current_digit % 10)
    if carry > 0:
        output.append(carry)
    return output

def format(output):
    output = [str(x) for x in output[::-1]]
    output = "".join(output)
    return output

def multiplication(num1,num2):
    carry = num1
    int2 = int(format(num2))
    for x in range(int2-1):
        carry = addition(num1,carry)
        print(carry)
        print(num1)
    return carry


# num3 = addition(num1,num2)
# print(format(num3))
num4 = multiplication(num1,num2)
print(format(num4))