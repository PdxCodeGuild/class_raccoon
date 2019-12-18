'''
Filename: lab_arbitrary.py
Author: Dylan
Purpose: make computer add like kids doing math in school(?)
'''

def arith(num1,num2):
    num_list = [num1,num2]
    num_list.sort()
    total = 0
    num1_rev = str(num1)[::-1]
    num2_rev = str(num2)[::-1]


    return total

#returns sum and remainder
def add(num1,num2):
    total = 0 
    remainder = 0
    temp_total = num1 + num2
    if temp_total < 10:
        total = temp_total
    else:
        total = temp_total % 10
        remainder = temp_total / 10
    return [total, remainder]


print(arith(23422340923410340239482304,303003025050020203492))