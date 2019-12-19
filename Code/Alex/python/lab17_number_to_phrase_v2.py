'''
Lab 17: Number to Phrase

Version 2

Handle numbers from 100-999.
'''
#user enters the number. this time it can be up to 999.
number = int(input("\n\n\n\n\n\n\n\n\n\nEnter a number below 1000: "))

ones_digit = number % 10#same as before
tens_digit = number % 100 // 10 #this changed since we now may need the remainder from the hundreds digit to calculate the tens digit.
hundreds_digit = number // 100 #can you see the cycle?

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

#im using a function to define our two variables being used.
def num_to_word(hundreds_digit, tens_digit):
    if number == 0:
        return "\"zero\""
    word = ''

    if hundreds_digit >= 1:
        word += f"{hundreds_digit_dict[hundreds_digit]}"
        if tens_digit == 0:
            word += f"{ones_digit_dict[ones_digit]}"
        elif tens_digit == 1:
            word += f"{teens_dict[ones_digit]}"
        elif tens_digit > 1:
            word += f"{tens_digit_dict[tens_digit]}-{ones_digit_dict[ones_digit]}"

    if hundreds_digit == 0:
        if tens_digit == 0:
            word += f"{ones_digit_dict[ones_digit]}"
        elif tens_digit == 1:
            word += f"{teens_dict[ones_digit]}"
        elif tens_digit > 1:
            word += f"{tens_digit_dict[tens_digit]}-{ones_digit_dict[ones_digit]}"
    return word

#now we are assigning the function to a variable so that we can call it later.
final_conversion = num_to_word(hundreds_digit, tens_digit)

print(f"\nYou spell that number like \"{final_conversion}\"\n\n\n")#now we call the solutions. and print the final result.
