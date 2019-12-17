# lab14_creditcard.py
# prompt user
cc = input("Card info: ")
card_info = list(cc)
for num in range(len(card_info)):
    card_info[num] = int(card_info[num])
print(type(card_info))

# Slice and check digits
check_digits = card_info.pop(-1)
print(check_digits)
print(card_info)

# reverse
card_info.reverse()
print(card_info)

# double every number
for num in range(len(card_info)):
    if num %2 == 0:
        card_info[num] = 2*card_info[num]
    else:
        card_info[num] = 2*card_info[num]
print(card_info)

# subtract nine from numbers over nine
for num in range(len(card_info)):
    if num > 9:
        card_info[num] = card_info[num] - 9
    else:
        card_info[num] = card_info[num]


# sum all
card_info = sum(card_info)

print(card_info)
print(check_digits)

# Check if last digit matches
if card_info % 10 == check_digits:
        print("Match.")
else:
        print("No Match.")
