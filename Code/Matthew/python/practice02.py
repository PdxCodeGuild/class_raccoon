
import string

# i = 0
# while i < 10:
#     print('loop')
#     i += 1
#
# for i in range(10): # 0,1,2,3,4,5,6,7,8,9
#     print('loop')
#
# for i in range(5, 10): # 5,6,7,8,9
#     ...
#
# for i in range(5, 10, 2): #5,7,9
#     ...
#
# fruits = ['apples', 'bananas', 'pears']
# for fruit in fruits: # iterate over the elements
#     print(fruit)
#
# for i in range(len(fruits)): # iterate over the indices
#     print(fruits[i])
#
# letters = 'abcdefg'
# for letter in letters: # iterate over the characters
#     print(letter)
#
# for i in range(len(letters)): # iterate over the indices
#     print(letters[i])
#



# word = 'hello'
# print(word[0]) # h
# print(word[1:3]) # el
# print(word[:3]) # hel
# print(word[3:]) # llo
#
#
#
# exit()





def double_letters(word):
    double = ''
    for letter in word:
        double += letter * 2
    return double

# print(double_letters('yay')) # hheelllloo




# Problem 2
# Write a function that takes a string, and returns a list of strings, each missing a different character.

def missing_char(word):
    # out_list = []
    # for i in range(len(word)):
    #     word_list = list(word)
    #     word_list.pop(i)
    #     word_out = ''.join(word_list)
    #     out_list.append(word_out)
    # return out_list

    out_list = []
    for i in range(len(word)):
        word_out = word[:i] + word[i+1:]
        out_list.append(word_out)
    return out_list

# print(missing_char('kitten')) # ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']





def latest_letter(word):
    # letters = list(word)
    # letters.sort()
    # return letters[-1]
    # # letters.sort(reverse=True)
    # # return letters[0]

    alphabet = list(string.ascii_lowercase)
    alphabet.sreverse()
    for letter in alphabet:
        if letter in word:
            return letter


# print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v












# s = 'hello world goodbye world'
# print(s.find('world')) # 6
# print(s.find('hi')) # -1
# print(s.find('world', 10)) # 20

# Problem 4
# Write a function that returns the number of occurances of 'hi' in a given string.
def count_hi(text):
    # return text.count('hi')

    # count = -1
    # hi_index = 0
    # while hi_index != -1:
    #     hi_index = text.find('hi', hi_index)
    #     hi_index += 1
    #     count += 1

    count = 0
    hi_index = 0
    while True:
        hi_index = text.find('hi', hi_index)
        if hi_index == -1:
            break
        else:
            count += 1
            hi_index += 1

    return count


def count_hi2(text):
    count = 0
    for i in range(len(text)-1):
        if text[i] == 'h' and text[i+1] == 'i':
            count += 1
    return count


# print(count_hi('hello world!'))
# print(count_hi('hihi')) # 2
# print(count_hi('hi20939489039224ljklekfkjasdfhi')) # 2
# print(count_hi('321hihi123hi')) # 3



def count_occurances2(text, word):
    # count = 0
    # for i in range(len(text)-2):
    #     if text[i] == word[0] and text[i+1] == word[1] and text[i+2] == word[2]:
    #         count += 1
    # return count

    count = 0
    for i in range(len(text)-len(word)+1):
        # print(text[i:i+len(word)])
        if text[i:i+len(word)] == word:
            count += 1
    return count


def count_occurances3(text, word):
    count = 0
    for i in range(len(text)-len(word)+1):
        match = True
        for j in range(len(word)):
            if text[i+j] != word[j]:
                match = False
                break
        if match:
            count += 1
    return count




# print(count_hi2('hello world!'))
# print(count_hi2('hihi')) # 2
# print(count_hi2('hi20939489039224ljklekfkjasdfhi')) # 2
# print(count_hi2('321hihi123hi')) # 3

def count_occurances(text, word):
    count = 0
    found_index = 0
    while True:
        found_index = text.find(word, found_index)
        if found_index == -1:
            break
        else:
            count += 1
            found_index += 1

    return count



# print(count_occurances3('hello world!', 'hi')) # 0
# print(count_occurances3('hihi', 'hi')) # 2
# print(count_occurances3('hi20939489039224ljklekfkjasdfhi', 'hi')) # 2
# print(count_occurances3('321hihi123hi', 'hi')) # 3
# print(count_occurances3('the only thing ever that the thing', 'the')) # 2


# Problem 5
# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'
def cat_dog(text):
    return count_occurances(text, 'cat') == count_occurances(text, 'dog')
print(cat_dog('catdog')) # True
print(cat_dog('catcat')) # False
print(cat_dog('catdogcatdog')) # True







# 'Teddy'
# 'Tim'
# 'Curt'
# 'Daniel'
# 'Johnny'
# 'Brandon'
# 'Alex'
# 'Dylan'
# 'Holden'
#
# # Student Sorter
#
# students = ['']
