'''
Filename: lab_arbitrary.py
Author: Dylan
Purpose: make computer add like kids doing math in school(?)
'''

import helper 


def arith(num1,num2):
    total = 0
    num1_rev = str(num1)[::-1]
    num2_rev = str(num2)[::-1]

    greater_length = 0
    if len(str(num1)) > len(str(num2)):
        greater_length = len(str(num1))
    else:
        greater_length = len(str(num2))
    carry = 0
    place = 1
    for i in range(greater_length): #greater length so it doesn't stop early 
        temp_sum = 0 
        if i < len(num1_rev): #if i is larger than the num length, we don't want any action or we'll get an error
            int1 = int(num1_rev[i])
            temp_sum += int1
        if i < len(num2_rev):
            int2 = int(num2_rev[i])
            temp_sum += int2
        if temp_sum < 10:
            total += ((temp_sum + carry) * place) #place variable allows us to multiply by 10^whatever level we're at
            carry = 0 #the carry amount gives us last rouund's remainder. Must reset to 0 each time, or it'll go too high. 
        else:
            carry = temp_sum / 10 
            temp_sum = temp_sum % 10
            total += temp_sum * place
        place *= 10  
    return total   

if __name__ == "__main__":
    print("Welcome to adding numbers!")
    cont = 'y'
    while cont == 'y':
        print("What is your first number to add?")
        num1 = helper.digit_checker(input("> "))
        print("What is your second number?")
        num2 = helper.digit_checker(input("> "))
        print(f"Your total is: {arith(num1,num2)}.")
        print("\nGo again? (y/n)")
        cont = input("> ").lower()
