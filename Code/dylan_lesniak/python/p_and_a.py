'''
Filename: p_and_a.py
Author: Dylan 
Purpose: Analyze palindromes and anagrams
File_nickname: ezpz
'''

import string

punctuation = string.punctuation
digits = string.digits
whitespace = string.whitespace

def is_palindrome(word1):
    return word1.lower() == word1[::-1].lower()

def is_anagram(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = [char for char in str1 if char not in punctuation and char not in digits and char not in whitespace]
    str2_list = [char for char in str2 if char not in punctuation and char not in digits and char not in whitespace]
    str1_list.sort()
    str2_list.sort()
    return "".join(str1_list) == "".join(str1_list)

if __name__ == "__main__":
    print("What is your first word? ")
    str1 = input("> ")
    print("What is your second word? ")
    str2 = input("> ")
    print()
    print(f"Word 1 is a palindrome: {is_palindrome(str1)}")
    print(f"Word 2 is a palindrome: {is_palindrome(str2)}\n")
    print(f"Word 1 and Word 2 are anagrams: {is_anagram(str1,str2)}")

    