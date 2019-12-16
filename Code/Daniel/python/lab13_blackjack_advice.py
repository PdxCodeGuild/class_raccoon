print("Please input your three cards")
card_counter = 0
card_total = 0
card_total_ace = 0
card_list = []
card_list_ace = []
while card_counter < 3:
    user_input = input("Insert card: ").lower()
    if user_input == "a":
        card_list.append(1)
        card_list_ace.append(11)
    elif user_input in ["j", "q" , "k"]:
        card_list.append(10)
        card_list_ace.append(10)
    else:
        card_list.append(int(user_input))
        card_list_ace.append(int(user_input))
    card_counter += 1
card_total = card_list[0] + card_list [1] + card_list[2]
card_total_ace = card_list_ace[0] + card_list_ace[1] + card_list_ace[2]
if card_total_ace < 21:
    card_total = card_total_ace


    
if card_total <= 17:
    print(f"Your total is {card_total}, hit.")
elif 17 < card_total < 20:
    print(f"Your total is {card_total}, stay.")
elif card_total == 21:
    print(f"Your total is {card_total}, blackjack!")
else:
    print(f"Your total is {card_total}, busted!")