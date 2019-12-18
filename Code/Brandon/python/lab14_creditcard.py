#credit card validation


# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.



# Convert the input string into a list of ints
credit_number = list(input("Please input your credit card number\n:"))

def credit_int(credit_number):
    for i in range (0, len(credit_number)):
        credit_number[i] = int(credit_number[i])
    return credit_number
print(credit_int(credit_number))
#---------------------------------------------------
# Slice off the last digit. That is the check digit.
print (credit_number.pop())
#---------------------------------------------------
#Reverse the digits.
new_list = credit_number[::-1]
print(new_list)
#----------------------------------------------------
# Double every other element in the reversed list.






