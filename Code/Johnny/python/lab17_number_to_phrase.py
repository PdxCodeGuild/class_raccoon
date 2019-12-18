# lab17_number_to_phrase.py

# created a dictionary with int as key and result strings
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
    10 : 'ten'
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
    2 : 'twenty',
    3 : 'thirty',
    4 : 'fourty',
    5 : 'fifty',
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    9 : 'ninety'
}

# prompt for number from user
user_input = int(input("Enter a number: "))
# create a string for input
# grab digit and break it apart to get first and second digits
# call key from dictionary
x = user_input
y = x//10
z = x%10
print(f'User input: {x}')
print(f'Tens digit: {y}')
print(f'Single digit: {z}')

# if conditions to find keys from dictionary and print results
if y >= 2:
    if z == 0:
        print(f">>> {tens[y]} <<<")
    else:
        z >= 1
        print(f">>> {tens[y]}-{ones[z]} <<<")
elif y == 1:
    if z > 0:
        print(f'>>> {teens[z]} <<<')



"""
EXAMPLE
x = 67 # user inputs
tens_digit = x//10 # returns '6'
ones_digit = x%10 # returns '7'
print(x)
print(tens_digit)
print(ones_digit)
"""
