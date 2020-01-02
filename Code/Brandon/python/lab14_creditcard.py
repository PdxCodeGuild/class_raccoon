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
list_2 = new_list
for i in range(0,len(new_list),2):
    new_list[i] *= 2
print (f"Here is the new list with all the numbers doubled\n{list_2}")
#---------------------------------------------------
# Subtract nine from numbers over nine.
for i in range(len(list_2)): #iterates over each i in list2
    list_2[i] = int(list_2[i]) #converts the i to int
    if list_2[i] >= 10: #if the i in list2 is greater than or equal to 10 it will subtract 9
        list_2[i] -= 9
print (f"Here is the new list subtracting 9 from numbers over 9\n{list_2}") #if it wasnt greater than 10 it stays the same.
#---------------------------------------------------
# Sum all values of the list2
sum_nums = str(sum(list_2))
print(sum_nums)
#---------------------------------------------------
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
def validate(x,y):
    if int(x[1]) == int(y) :
        print("Valid entry")
    else:
        print("does not validate")

validate(sum_nums,check_digit)
