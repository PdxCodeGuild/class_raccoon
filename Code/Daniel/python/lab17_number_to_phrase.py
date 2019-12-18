# turn numbers into their word counterparts
# libraries to convert numbers into phrases (also, teen numbers are stupid)
single_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens_digit = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
double_digits = ["ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
triple_digit = ["one hundred and", "two hundred and", "three hundred and", "four hundred and", "five hundred and", "six hundred and", "seven hundred and", "eight hundred and", "nine hundred and"]
#libraries to convert numbers into roman numerals
roneslist = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
rtenslist = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
rhundolist = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]


user_input = (int(input("Pick a number from 0-999: ")))

return_number = ""
return_number_roman = ""

#logic to break out values between 100-999
hundredsdigit = user_input // 100
user_input = user_input % 100
#same as above but for 10-99 and 0-9
tensdigit = user_input // 10
onesdigit = user_input % 10

#logic to take the values from above and convert them into their component phrases
if user_input == 0:
    return_number = "0"
elif tensdigit == 0:
    return_number = single_digits[onesdigit]
elif tensdigit == 1 and onesdigit == 0:
    return_number = "ten"
#like I said, teen numbers are stupid
elif tensdigit == 1:
    return_number = teens_digit[onesdigit-1]
elif hundredsdigit >= 1:
    return_number = triple_digit[hundredsdigit-1] + " " + double_digits[tensdigit-1] + " " + single_digits[onesdigit]
elif 1 < tensdigit :
    return_number = double_digits[tensdigit-1] + " " + single_digits[onesdigit]



#same as logic above, but for roman numerals (also simpler because no teen numbers)
if user_input == 0:
    return_number_roman = "none"
elif tensdigit == 0:
    return_number_roman = roneslist[onesdigit]
elif tensdigit >= 1 and hundredsdigit == 0:
    return_number_roman = rtenslist[tensdigit] + roneslist[onesdigit]
elif hundredsdigit > 0:
    return_number_roman = rhundolist[hundredsdigit] + rtenslist[tensdigit] + roneslist[onesdigit]

print(f"The number you selected is {return_number} or {return_number_roman} in roman numerals")
