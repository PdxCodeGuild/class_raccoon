'''
Lab 17: Number to Phrase

Version 2

Handle numbers from 100-999.
'''

number = int(input("Enter a number below 1000: "))


ones_digit = number % 10
tens_digit = number % 100 // 10
hundreds_digit = number // 100

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

hundreds_digit_dict = {
1: 'one hundred ',
2: 'two hundred ',
3: 'three hundred ',
4: 'four hundred ',
5: 'five hundred ',
6: 'six hundred ',
7: 'seven hundred ',
8: 'eight hundred ',
9: 'nine hundred ',
}

def num_to_word(hundreds_digit, tens_digit):

    word = ''

    if hundreds_digit >= 1:
        word += f"\"{hundreds_digit_dict[hundreds_digit]}"

        if tens_digit == 0:
            word += f"{ones_digit_dict[ones_digit]}\""

        elif tens_digit == 1:
            word += f"{teens_dict[ones_digit]}\""

        elif tens_digit > 1:
            word += f"{tens_digit_dict[tens_digit]}-{ones_digit_dict[ones_digit]}\""


    if hundreds_digit == 0:

        if tens_digit == 0:
            word += f"{number} is spelled \"{ones_digit_dict[ones_digit]}\""

        elif tens_digit == 1:
            word += f"{number} is spelled \"{teens_dict[ones_digit]}\""

        elif tens_digit > 1:
            word += f"{number} is spelled \"{tens_digit_dict[tens_digit]}-{ones_digit_dict[ones_digit]}\""

    return word

num_to_text = num_to_word(hundreds_digit, tens_digit)
print(f"Your number to words is {num_to_text}")
