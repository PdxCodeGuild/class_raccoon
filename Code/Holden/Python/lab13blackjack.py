cardlist=["dead", "a", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]
card1 = "0"
card2 = "0"
card3 = "0"
while True:
    card1=input("Please input the first card: ").lower()
    if card1 in cardlist:
        break
    print("Please input valid card.")
while True:
    card2=input("Please input the second card: ").lower()
    if card2 in cardlist:
        break
    print("Please input valid card.")
while True:
    card3=input("Please input the third card: ").lower()
    if card3 in cardlist:
        break
    print("Please input valid card.")
if cardlist.index(card1) > 10:
    card1 = "10"
if cardlist.index(card2) > 10:
    card2 = "10"
if cardlist.index(card3) > 10:
    card3 = "10"
output = cardlist.index(card1) + cardlist.index(card2) + cardlist.index(card3)
acecount=0
if card1 == "a":
    output += 10
    acecount +=1
if card2 == "a":
    output += 10
    acecount +=1
if card3 == "a":
    output += 10
    acecount +=1
while output != 21 and acecount > 0:
    output -= 10
    acecount -= 1
if output > 21:
    print(f"{output}, already busted.")
elif output == 21:
    print("Blackjack!")
elif output >= 17:
    print(f"{output}, stay.")
else:
    print(f"{output}, hit.")
