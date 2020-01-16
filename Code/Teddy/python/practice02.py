import string

'''Practice 2: Strings

For each practice problem, write a function that returns a value (not just prints it).
You can then call the function a couple times to test it, comment those calls out,
and move on to the next problem. An example of this format is given below.

def add(a, b):
    return a + b
#print(add(5, 2))
#print(add(8, 1))

'''

'''Problem 1'''
# Get a string from the user, print out another string, doubling every letter.
'''
def double_letters(word):
    double = ''
    for letter in word:
        double += letter *2
    return double

print(double_letters('hello')) # hheelllloo
'''
#**********************************************************************

'''Problem 2'''
# Write a function that takes a string, and returns a list of strings, each missing a different character.
'''
def missing_char(word):
    out_list = []
    for i in range(len(word)):
        word_list = list(word)
        word_list.pop(i)
        word_out = ''.join(word_list)
        out_list.append(word_out)
    return out_list

print(missing_char('kitten')) # ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']
'''
#**********************************************************************

'''Problem 3'''
# Return the letter that appears the latest in the english alphabet.
'''
def latest_letter(word):
    letters = list(word)
    letters.sort()
    return letters[-1]

print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v
'''
#**********************************************************************

'''Problem 4'''
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
  ...
print(count_hi('hihi')) # 2


'''Problem 5'''
# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

def cat_dog(text):
  pass
print(cat_dog('catdog')) # True
print(cat_dog('catcat')) # False
print(cat_dog('catdogcatdog')) # True
