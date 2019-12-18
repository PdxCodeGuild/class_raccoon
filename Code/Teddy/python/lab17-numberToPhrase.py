'''
Lab 17: Number to Phrase
Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings.
'''
# setup ones digits
numberOne = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
}
# setup tens digits
numberTen = {
    1 : 'Ten',
    2 : 'Twenty',
    3 : 'Thirty',
    4 : 'Forty',
    5 : 'Fifty',
    6 : 'Sixty',
    7 : 'Seventy',
    8 : 'Eighty',
    9 : 'Ninety',
}
# setup teen digits
numberTeen = {
    11 : 'Eleven',
    12 : 'Twelve',
    13 : 'Thirteen',
    14 : 'Fourteen',
    15 : 'Fifteen',
    16 : 'Sixteen',
    17 : 'Seventeen',
    18 : 'Eighteen',
    19 : 'Nineteen'
}

# Set condition
play_again = 'y'

# Loop if condition is 'y'
while play_again == 'y':

    # user promt
    user_input = int(input('Input number between 0 and 99: '))

    # Get the tens digit
    tens_digit = user_input//10

    # Get the ones digit
    ones_digit = user_input%10

    # If the user_input is btw 0 and 10
    if 0 <= user_input < 10:
        output = numberOne[user_input]

    # If the user_input is 10
    elif user_input == 10:
        output = numberTen[1]

    # If the user_input is btw 0 and 10
    elif 10 < user_input < 20:
        output = numberTeen[user_input]

    # If user_input btw 20 and 1000
    elif 20 <= user_input < 100:
        output = f'{numberTen[tens_digit]}-{numberOne[ones_digit]}'
    print(output)

    # Display output
    play_again = input('Play again (y/n)? ').lower()

# get out from while loop if the user say no(n)
else:
    print('Bye')
