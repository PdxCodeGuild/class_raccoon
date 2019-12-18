#turn numbers into their word counterparts

single_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens_digit = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
double_digits = ["ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
triple_digit = ["one hundred and", "two hundred and", "three hundred and", "four hundred and", "five hundred and", "six hundred and", "seven hundred and", "eight hundred and", "nine hundred and"]
user_input = (int(input("Pick a number from 0-999: ")))

hundredsdigit = user_input // 100
user_input = user_input % 100
tensdigit = user_input // 10
onesdigit = user_input % 10

if user_input == 0:
    print("zero")
elif tensdigit == 0:
    print(single_digits[onesdigit])
elif tensdigit == 1 and onesdigit == 0:
    print("ten")
elif tensdigit == 1:
    print(teens_digit[onesdigit-1])
elif hundredsdigit >= 1:
    print(triple_digit[hundredsdigit-1] + " " + double_digits[tensdigit-1] + " " + single_digits[onesdigit])
elif tensdigit > 1:
    print(double_digits[tensdigit-1] + " " + single_digits[onesdigit])
