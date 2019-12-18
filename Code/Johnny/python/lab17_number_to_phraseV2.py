ones = {
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
teens = {
    1 : 'eleven',
    2 : 'twelve',
    3 : 'thirteen',
    4 : 'fourteen',
    5 : 'fifteen',
    6 : 'sixteen',
    7 : 'seventeen',
    8 : 'eighteen',
    9 : 'nineteen'
}
tens = {
    1 : 'ten',
    2 : 'twenty',
    3 : 'thirty',
    4 : 'fourty',
    5 : 'fifty',
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    9 : 'ninety'
}
hundo = {
    1 : 'one hunderd',
    2 : 'two hundred',
    3 : 'three hundred',
    4 : 'four hundred',
    5 : 'five hundred',
    6 : 'six hundred',
    7 : 'seven hundred',
    8 : 'eight hundred',
    9 : 'nine hundred'
}

# prompt for number from user
user_input = int(input("Enter a number 0 - 999: "))
# create a string for input
# grab digit and break it apart to get first and second digits
# call key from dictionary
w = user_input
x = (w//10)//10
y = (w//10)%10
z = w%10

print(f'User input: {w}')
print(f'Hundo digit: {x}')
print(f'Tens digit: {y}')
print(f'Single digit: {z}')

# if conditions to find keys from dictionary and print results
if x >= 1 and y == 0 and z == 0:
    print(f'>>> {hundo[x]} <<<')
elif x >= 1 and y >= 2 and z >=1:
    print(f'>>> {hundo[x]} {tens[y]}-{ones[z]} <<<')
elif x >= 1 and y == 1:
    print(f'>>> {hundo[x]} {teens[z]} <<<')
elif x== 0 and y == 1 and z > 1:
    print(f'>>> {teens[z]} <<<')
elif x == 0 and y == 0  and z <= 10:
    print(f'>>> {ones[z]} <<<')
elif y >= 1 and z >= 0:
    print(f'>>> {tens[y]} <<<')
else:
    print(f'>>> I messed up somewhere... <<<')
