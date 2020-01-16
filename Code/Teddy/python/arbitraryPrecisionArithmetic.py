'''
Arbitrary Precision Arithmetic is a way of performing arithmetic with greater precision
than that offered by ordinary ints and floats. One python library for this is mpmath.

Addition
Remember doing long addition in elementary school? You could represent an 'big int' as a list of ints.
To add them, loop over the digits from 'right' to 'left', keeping track of the 'carry'.
Also be wary of numbers with differing number of digits. Prompt the user for each number and print out their sum.

What is the first number? 23422340923410340239482304
What is the second number? 303003025050020203492
23422340923410340239482304 + 303003025050020203492 = 23422643926435390259685796
Multiplication
A simple (but inefficient) way of implementing multiplication is through repeated addition.
For example, 564*6 = 564+564+564+564+564+564. A more efficient way would be long multiplication.
'''
first_number = []
second_nunber = []

while True:
    num1 = input('What is the first number? ')
    num2 = input('What is the seconde number? ')

    if num1.isdigit() and num2.isdigit():
        break
    else:
        print('Invalid inputs!!')

num1 = list(num1)
num2 = list(num2)

num1.reverse()
num2.reverse()

num1 = [int(x) for x in num1]
num2 = [int(x) for x in num2]

def addition(num1, num2):
    carry = 0
    output = []
    for i in range(len(num1)):
        current_digit = carry + num1[i] + num2[i]
        print(num1,num2,current_digit)
        carry = current_digit // 10
        output.append(current_digit % 10)
    if carry > 0:
        output.append(carry)
    return output

def print_output(output):
    output = [str(x) for x in output[::-1]]
    output = ''.join(output)

    print(carry)


addition(num1, num2)
