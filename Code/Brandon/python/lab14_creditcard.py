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
check_digit = credit_number.pop()
print (f"This removed the last number {check_digit}")
#---------------------------------------------------
#Reverse the digits.
new_list = credit_number[::-1]
print(f"Here is the reversed list \n{new_list}")
#----------------------------------------------------
# Double every other element in the reversed list.
list_2 = []
for i in range(len(new_list)):
    num = new_list[i] * 2
    list_2.append(num)
print (f"Here is the new list with all the numbers doubled\n{list_2}")
# Subtract nine from numbers over nine.
list_3 = []
for i in range(len(list_2)):
    list_2[i] = int(list_2[i])
    if i in list_2 >= 10:
        num = list_2[i] - 9
    else:
        num = list_2[i]
list_3.append(num)
print (f"Here is the new list subtracting 9 from numbers over 9\n{list_3}")
