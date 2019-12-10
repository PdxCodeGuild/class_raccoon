#lab06_password.py

#pw.py
import random
import string
import time

print("Welcome to the Password Generator!\n")

lower_c = list(string.ascii_lowercase)
upper_c = list(string.ascii_uppercase)
all_ltr = list(string.ascii_letters)
number_c = list(string.digits)
special_c = list(string.punctuation)
all_c = list(lower_c + upper_c + number_c + special_c)

#Version 1 & 2 - Make a rando password with while loop using length n
pass_w = ""
num_char = 1
total_n = "a"
while total_n.isdigit() == False:
    total_n = input("How many characters do you want in your password? ")
    if total_n.isdigit() == False:
        print("\nInvalid Entry! Numbers only.\n")
total_n=int(total_n)

while num_char < total_n:
    num_char = num_char + 1
    pass_w = pass_w + random.choice(all_c)
    print(pass_w)
    time.sleep(.2)

pass_w = pass_w + random.choice(all_c)
print(f"Here's your 'random' password:\n{pass_w}\n")
input("Press ENTER to continue\n")

#Version 3 - User chooses number of characters by type
pass_w = ""
print("Let's try something different!\nThis time you choose how many of each character type you want.\n")
let_char = input("How many letters do you want? ")
let_char = int(let_char)
num_char = input("How many numbers do you want? ")
num_char = int(num_char)
sp_char = input("How many special characters do you want? ")
sp_char = int(sp_char)

all_let = lower_c + upper_c
letter_s = ""
for x in range(let_char):
    letter_s = letter_s + random.choice(all_let)

number_s = ""
for x in range(num_char):
    number_s = number_s + random.choice(number_c)

special_s = ""
for x in range(sp_char):
    special_s = special_s + random.choice(special_c)

pw_list = list(letter_s + number_s + special_s)
random.shuffle(pw_list)
pw_list = "".join(pw_list)

pw = ""
num_char = 1
char_ct = 0
while num_char < len(pw_list):
    pw = pw + pw_list[char_ct]
    char_ct += 1
    print(pw)
    num_char += 1
    time.sleep(.2)

print("\n Your 'random' password is:")
print(pw_list)
