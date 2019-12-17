while True:
    card=input("Please input credit card number: ")
    if card.isdigit() and len(card) == 16:
        break
    print("Please input a 16 long string of digits")
cardlist = list(card)
for i in range(len(cardlist)):
    cardlist[i] = int(cardlist[i])
check = int(cardlist.pop(15))
cardlist.reverse()
for i in range(0,len(cardlist),2):
    cardlist[i] = (cardlist[i]*2)
sum = 0
for i in range(len(cardlist)):
    if cardlist[i] > 9:
        cardlist[i] = cardlist[i]-9
    sum += cardlist[i]
print(check == sum%10)
#4556737586899855
