import string
import os

os.system('cls')

card_number = list(input('Enter your 16 digit card number\n> '))
check_dig = card_number[-1]
card_number.pop(-1)
card_number.reverse()
double_list = []
odd_list = []
step_five = []

# Getting the odd numbered elements of the reversed list
def get_odd_index(card_number):
    for i in card_number:
        double_list.append(int(i)*2)
    for i in range(len(double_list)):
        if i%2 == 1:
            odd_list.append(double_list[i])
get_odd_index(card_number)

for i in odd_list:
    if i > 9:
        step_five.append(i - 9)
    else:
        step_five.append(i)

checksum = sum(step_five)
if checksum%10 == check_dig:
    print('Good card, bro')
else:
    print('Bad card. Sorry')
