'''
Lab 15: ROT Cipher

Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
'''

import string
#i imported the string to save some typing

alphabet = string.ascii_lowercase #this is our reference of organized letters
user_string = input("Yo. gimme a string of letters and i will encode it ROT13 style  ")#this is the mash of letters we need to organize and alter

password = ''# we did this because we are dealing with strings and we need to define what the new password will be

for i in range(len(user_string)):#for each indicy in the range of the length of the users mashed input of letters
    index_i = alphabet.find(user_string[i])#now we define the index of the user's letter "user_string[i]" by finding it in the alphabet of letters(our main reference)
    index_i += 13#we take that index and add and equal it to the index 13 indicies in front of it. so now we have our new letter
    password += alphabet[index_i%26]#now we take the letter which can be past index 26 of the alphabet and we mod it through the list of letters again and again to give us a letter every time.

print(password)#the new letters
