'''
Filename: lab14_card_validation.py
Author: Dylan
Purpose: returns a boolean whether string is valid credit card entry
'''

def validate(card):
    int_nums = []
    for num in card:
        if num.isdigit(): 
            int_nums.append(int(num))
    
    check_digit = int_nums[-1]
    int_nums = slice_reverse_and_double(int_nums)
    int_nums = sub_and_add(int_nums)
    second_digit = int_nums % 10
    return second_digit == check_digit

def slice_reverse_and_double(int_nums):
    int_nums = int_nums[:-1]
    int_nums.reverse()
    for i in range(len(int_nums)):
        if i % 2 == 0:
            int_nums[i] *= 2
    return int_nums

def sub_and_add(int_nums):
    for i in range(len(int_nums)):
        if int_nums[i] > 9:
            int_nums[i] -= 9
    sum_values = 0
    for num in int_nums:
        sum_values += num
    return sum_values

print (validate("4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5"))