#lab13_blackjack.py

#define cards
cardlist = ["A"]
for i in range(1,11):
    i = str(i)
    cardlist.append(i)
cardlist.extend(["J","Q","K"])
print(cardlist)

valuelist = [1]
for i in range(1,11):
    valuelist.append(i)
valuelist.extend([10,10,10])
print(valuelist)

#function for converting to number
def card_chk(question):
    cardnum = ""
    while cardnum not in cardlist:
        cardnum = input(f"{question}").upper()
    cardnum_val = valuelist[cardlist.index(cardnum)]
    return [cardnum_val, cardnum]

card1 = card_chk("What's your first card? ")
print (card1)
card2 = card_chk("What's your second card? ")
print (card2)
card3 = card_chk("What's your third card? ")
print (card3)

cardtotal = card1[0] + card2[0] + card3[0]

def advice(cardtotal):
    if cardtotal < 17:
        print(f"{cardtotal} Hit")
    elif cardtotal == 21:
        print(f"{cardtotal} Blackjack!")
    elif cardtotal > 21:
        print(f"{cardtotal} Dude, you're so busted!")
    else:
        print(f"{cardtotal} Stay")

print("Here's your possible values:")
advice(cardtotal)

#Version 2
def acechk(cardtotal):
    for card in cardface:
        if card == "A":
            cardtotal += 10
        advice(cardtotal)

cardface = [card1[1], card2[1], card3[1]]
acechk(cardtotal)
