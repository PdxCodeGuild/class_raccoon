card_number = []
card_number = input("Please insert your credit card number: ")
#Convert the input string into a list of ints
card_number.split()
card_number = list(card_number)
for num in range(len(card_number)):
    card_number[num] = int(card_number[num])
# Slice off the last digit. That is the check digit.
chk_digit = card_number[-1]
card_number = card_number[:-1]
# Reverse the digits.
card_number.reverse()
# Double every other element in the reversed list.
for i in range(0, len(card_number), 2):
    card_number[i] *= 2
# Subtract nine from numbers over nine.
for num in range(len(card_number)):
    if card_number[num]> 9:
        card_number[num] = card_number[num] - 9
print(card_number)
# Sum all values.
card_number = sum(card_number)
card_number = str(card_number)
card_number_2 = [int(x) for x in str(card_number)]
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
if card_number_2[1] == chk_digit:
    print("Valid input")
else:
    print("Invalid input")