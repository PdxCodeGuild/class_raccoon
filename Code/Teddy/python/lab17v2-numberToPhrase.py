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
    tens_digit = num // 10 % 10
    ones_digit = num % 10

    print(tens_digit)

    if tens_digit == 0:
        if ones_digit == 0:
            return numberHundred[hundreds_digit]
        else:
            return numberHundred[hundreds_digit] + ' and ' + numberOne[ones_digit]



user_input = int(input('What is the number? '))

if user_input < 100:
    print(getTens(user_input))
elif user_input < 1000:
    print(getHundreds(user_input))
else:
    print('Please input numbers 0-999')
