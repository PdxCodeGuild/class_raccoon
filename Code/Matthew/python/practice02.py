
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
    alphabet.reverse()
    for letter in alphabet:
        if letter in word:
            return letter
    
    
print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v



