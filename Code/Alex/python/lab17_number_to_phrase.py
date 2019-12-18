'''
Lab 17: Number to Phrase

Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10

Hint 2: use the digit as an index for a list of strings.
'''

number = int(input("Enter a number below 100: "))


ones_digit = number % 10
tens_digit = number // 10

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
