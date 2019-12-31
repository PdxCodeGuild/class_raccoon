#lab14_creditcard.py

print("Credit Card Validator")

c_card = "."
while c_card.isdigit() == False:
    c_card = input("What's your credit card number? ").replace(" ","")

#Step 1 - List of Ints
cardlist = list(c_card)
for num in range(len(cardlist)):
    cardlist[num] = int(cardlist[num])
print(cardlist)

#Step 2 - Slice off last digit
checkdig = cardlist.pop(-1)
print(cardlist)

#Step 3 - Reverse it
cardlist.reverse()
print(cardlist)

#Step 4 - Double every other
for num in range(len(cardlist)):
    if (num % 2) == 0:
        cardlist[num] = 2*cardlist[num]
print(cardlist)

#Step 5 - Sub 9 from numbers over nine
for num in range(len(cardlist)):
    if cardlist[num] > 9:
        cardlist[num] = cardlist[num] - 9
print(cardlist)

#Step 6 - Sum all values
sum_val = sum(cardlist)
print(sum_val)

#Step 7 - Second digit
sum_val = str(sum_val)
second = int((sum_val[1]))
print(second)

#Step 8 - Check if valid
if second == checkdig:
    print("Valid!")
else:
    print("Invalid!")
