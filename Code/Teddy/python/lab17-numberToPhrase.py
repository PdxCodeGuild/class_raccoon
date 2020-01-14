'''
Lab 17: Number to Phrase
Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings.
'''

'''
# setup ones digits
numberOne = {
    0 : 'Zero',
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine',
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
# setup digits of 11 to 19
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
# setup digits of 100 to 999
numberHundred = {
    1 : 'One hundred',
    2 : 'Two hundred',
    3 : 'Three hundred',
    4 : 'Four hundred',
    5 : 'Five hundred',
    6 : 'Six hundred',
    7 : 'Seven hundred',
    8 : 'Eight hundred',
    9 : 'Nine hundred'
}

# Set condition
play_again = 'y'

# Loop if condition is 'y'
while play_again == 'y':

    # user promt
    user_input = int(input('Input number between 0 and 999: '))

    # Get the tens digit
    hundreds_digit = user_input//100

    teens_digit = user_input%100

    # Get the tens digit
    tens_digit = user_input//10%10
    print('============')
    print(tens_digit)

    # Get the ones digit
    ones_digit = user_input%10

    # If the user_input is btw 0 and 10
    if 0 <= user_input < 100:
        if 0 <= user_input < 10:
            output = numberOne[user_input]

        # If the user_input is 10
        elif user_input == 10:
            output = numberTen[1]

        # If the user_input is btw 0 and 10
        elif 10 < user_input < 20:
            output = numberTeen[teens_digit]

        # If user_input btw 20 and 99
        elif 20 <= user_input < 100:
            output = f'{numberTen[tens_digit]}-{numberOne[ones_digit]}'

    # If user_input btw 100 and 999
    elif 100 <= user_input < 1000:
        # If the user_input is 100
        if user_input == 100:
            output = f'{numberHundred[1]}'

        # If the user_input is btw 0 and 10
        elif 100 < user_input < 200:
            if 100 < user_input < 110:
                output = f'{numberHundred[hundreds_digit]} and {numberOne[ones_digit]}'
            elif user_input == 110:
                output = f'{numberHundred[hundreds_digit]} and {numberTen[1]}'
            elif 110 < user_input < 120:
                output = f'{numberHundred[hundreds_digit]} and {numberTeen[teens_digit]}'
        #
        # # If user_input btw 20 and 99
        # elif 20 <= user_input < 100:
        #     output = f'{numberTen[tens_digit]}-{numberOne[ones_digit]}'






    # elif 100 <= user_input < 1000:
    #     output = f'{numberHundred[hundreds_digit]} {numberTen[tens_digit]}-{numberOne[ones_digit]}'

    print(output)

    # Display output
    play_again = input('Play again (y/n)? ').lower()

# get out from while loop if the user say no(n)
else:
    print('Bye')
'''
'''
# alternatively, use a dictionary: ones = {0:'zero', 1:'one', 2:'two'
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['zeroty', 'onety', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
'''
# setup ones digits
numberOne = {
    0 : 'Zero',
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine',
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
# setup digits of 11 to 19
numberTeen = {
    0 : 'Ten',
    1 : 'Eleven',
    2 : 'Twelve',
    3 : 'Thirteen',
    4 : 'Fourteen',
    5 : 'Fifteen',
    6 : 'Sixteen',
    7 : 'Seventeen',
    8 : 'Eighteen',
    9 : 'Nineteen'
}
# setup digits of 100 to 999

numberHundred = {
    1 : 'One hundred',
    2 : 'Two hundred',
    3 : 'Three hundred',
    4 : 'Four hundred',
    5 : 'Five hundred',
    6 : 'Six hundred',
    7 : 'Seven hundred',
    8 : 'Eight hundred',
    9 : 'Nine hundred'
}


def getTens(num):
    if num < 10:
        return numberOne[num]
    elif num < 20:
        return numberTeen[num-10]
    elif num < 100:
        tens_digit = num // 10
        ones_digit = num % 10
        if ones_digit == 0:
            return numberTen[tens_digit]
        else:
            return numberTen[tens_digit] + '-' + numberOne[ones_digit]

def getHundreds(num):

    hundreds_digit = num // 100
    tens_digit = num % 100
    ones_digit = num % 10

    if tens_digit == 0:
        return numberHundred[hundreds_digit]

    # hundreds_phrase = numberOne[hundreds_digit]+'-hundred'
    #
    # return hundreds_phrase + ' ' + getTens(tens_digit)



user_input = int(input('What is the number? '))

if user_input < 100:
    print(getTens(user_input))

elif user_input < 1000:
    print(getHundreds(user_input))
else:
    print('Please input numbers 0-999')
