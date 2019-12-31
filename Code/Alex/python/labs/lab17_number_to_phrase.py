'''
Lab 17: Number to Phrase

Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10

Hint 2: use the digit as an index for a list of strings.
'''

number = int(input("Enter a number below 100: "))#this is the number we are coding to convert to english.
#first we need to figure for a number below 100 so we will have a ones digit and tens digit.
ones_digit = number % 10#this makes the variable always a ones digit by finding the remainder of the number.
tens_digit = number // 10#this makes the variable always a tens digit because it erases the remainder(ones digit)

#i have a dictionary for the ones digits as they are spelled in English.
ones_digit_dict = {
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine',
}
#a dictionary of the tens digits in English
tens_digit_dict = {
2: 'twenty',
3: 'thirty',
4: 'fourty',
5: 'fifty',
6: 'sixty',
7: 'seventy',
8: 'eighty',
9: 'ninety',
}
#the exceptions for when (defined below) the ten digit = 1.
teens_dict = {
0: 'ten',
1: 'eleven',
2: 'twelve',
3: 'thirteen',
4: 'fourteen',
5: 'fifteen',
6: 'sixteen',
7: 'seventeen',
8: 'eighteen',
9: 'nineteen',
}

if tens_digit == 0:
    print(f"{number} is spelled \"{ones_digit_dict[ones_digit]}\"")

elif tens_digit == 1:
    print(f"{number} is spelled \"{teens_dict[ones_digit]}\"")

elif tens_digit > 1:
    print(f"{number} is spelled \"{tens_digit_dict[tens_digit]}-{ones_digit_dict[ones_digit]}\"")
