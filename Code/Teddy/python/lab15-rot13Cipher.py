'''
Lab 15: ROT Cipher
Write a program that prompts the user for a string, and encodes it with ROT13. For each character,
find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language,
so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m

'''
import string

max_len = 26
rot = 13

# User promt
user_input = input('Input the letters: ')
print(f'User input is {user_input}')

# converse string to list
user_input = list(user_input)
print(f'Put into the list {user_input}')

# Convese strings in the list to the list of ASCII number
ascii_list = []
for i in user_input:
    ascii_list.append(ord(i))
print(f'ASCII number is {ascii_list}')

# Encodes it with ROT13 by adding ASCII number with 13
r13 = []
for num in ascii_list:
    num -= ord('a')
    num += 13
    num %= 26
    num += ord('a')
    r13.append(num)
print(f'R13 number is {r13}')

# Convese the list of ASCII number to strings
str_list = []
for i in r13:
    if i >= ord('a') and i <= ord('z'):
        str_list.append(chr(i))
    # elif i > ord('z'):
    #     i = (i - ord('z')) + ord('a')
    #     str_list.append(chr(i))
    elif i >= ord('A') and i <= ord('Z'):
        str_list.append(chr(i))
    # elif i > ord('Z'):
    #     i = (i - ord('Z')) + ord('A')
    #     str_list.append(chr(i))




print(f'Translate list {str_list}')

new_char = ''.join(str_list)

print(new_char)


print(type(user_input))
