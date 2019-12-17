'''
Lab 14: Credit Card Validation
Let's write a function which returns whether a string containing a credit card number is valid as a boolean.
The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

card number = 4556737586899855
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
'''
# User input
card_numbers = input('Type 16 digits of your credit card numbers. ')
print(f'Card numbers {card_numbers}')

# Convert the input string into a list of ints
number_list = list(card_numbers)
print(f'Converse the card numbers to the list {number_list}')

# convert to ints
for i in range(len(number_list)):
    number_list[i] = int(number_list[i])

# Slice off the last digit. That is the check digit.
check_digit = number_list[-1]
number_slice = number_list[0:-1]
print(f'The check digit is {check_digit}')
print(f'Sliced of the last digit {number_slice}')

# Reverse the digits.
number_reverse = number_slice[::-1]
print(f'Reverse the numbers {number_reverse}')



# Double every other element in the reversed list.
for i in range(0, len(number_reverse), 2):
    number_reverse[i] = int(number_reverse[i])*2
number_double = number_reverse
print(f'Double the numbers {number_double}')

# Subtract nine from numbers over nine.
subtract_list = []
for i in number_double:
    if i > 9:
        number_subtract = i - 9

        subtract_list.append(number_subtract)
    else:
        subtract_list.append(i)
print(f'Subtract the numbers from 9 {subtract_list}')

# Sum all values.
number_sum = 0
for num in subtract_list:
    number_sum += num
print(f'Sum all numbers in the list {number_sum}')

# Take the second digit of that sum.
check_digit2 = number_sum % 10
print(f'The check digit is {check_digit2}')

# If the last digit of credit card matches the check digit, the whole card number is valid.
if check_digit == check_digit2:
    print('Valid')
else:
    print('Invalid')
