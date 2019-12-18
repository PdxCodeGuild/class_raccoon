
# English dictionary of numbers
english_dict = {
  1:'one',
  2:'two',
  3:'three',
  4:'four',
  5:'five',
  6:'six',
  7:'seven',
  8:'eight',
  9:'nine',
  10:'ten',
  11:'eleven',
  12:'twelve',
  13:'thirteen',
  14:'fourteen',
  15:'fifteen',
  16:'sixteen',
  17:'seventeen',
  18:'eighteen',
  19:'nineteen',
  20:'twenty',
  30:'thirty',
  40:'forty',
  50:'fifty',
  60:'sixty',
  70:'seventy',
  80:'eighty',
  90:'ninety',
}
# Roman dictionary of numbers
roman_dict = {
  1:'I',
  2:'II',
  3:'III',
  4:'IV',
  5:'V',
  6:'VI',
  7:'VI',
  8:'VIII',
  9:'IX',
  10:'X',
  20:'XX',
  30:'XXX',
  40:'XL',
  50:'L',
  60:'LX',
  70:'LXX',
  80:'LXXX',
  90:'XC',
}

# Get user choice for conversion
user_input = int(input("What number would you like to convert? (0-99)\n> "))
dict_choice = int(input("Would you like to convert to (1) English or (2) Roman?\n> "))

# Define function to convert number into English
def english_conversion(x):
    output = ''
    if x < 21:
        print(english_dict[user_input])
    elif x >= 21:
        tens_digit = english_dict[(user_input) - (user_input%10)]
        ones_digit = output + english_dict[user_input%10]
        output = tens_digit+' '+ones_digit
        print(output)

# Define function to convert numbers into Roman

# Define function to get the current time

# Output generation

if dict_choice == 1:
    english_conversion(user_input)
