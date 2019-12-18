#turn numbers into their word counterparts

single_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens_tigit = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
double_digits = ["ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
user_input = (int(input("Pick a number from 0-99: ")))

tensdigit = user_input // 10
onesdigit = user_input % 10

if user_input == 0:
    print("zero")
elif tensdigit == 0:
    print(single_digits[onesdigit])
elif tensdigit == 1 and onesdigit == 0:
    print("ten")
elif tensdigit == 1:
    print(teens_tigit[onesdigit-1])
elif tensdigit > 1:
    print(double_digits[tensdigit-1] + " " + single_digits[onesdigit])

    