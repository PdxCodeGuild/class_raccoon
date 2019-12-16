while True:
    card=input("Please input credit card number: ")
    if card.isdigit() and len(card) == 16:
        break
    print("Please input a 16 long string of digits")
cardlist = list(card)
check = int(cardlist.pop(15))
cardlist.reverse()
for i in range(0,len(cardlist),2):
    cardlist[i] = int(cardlist[i])*2
print(cardlist)
#4556737586899855
