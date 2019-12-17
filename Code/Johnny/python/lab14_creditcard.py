# lab14_creditcard.py

# input
card = []
check_digit = []
card_nums = input("Enter your credit card: ")

# convert to list

card_nums = list(card_nums)
print(card_nums)

# pop off last digit for check digit
check_digit1 = card_nums.pop(len(card_nums)-1)

# append last digit to the top list
check_digit.append(check_digit1)
print(check_digit)
print(card_nums)

# reverse list
card_nums.reverse()
print(card_nums)
