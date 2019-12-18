

# 
import string
# 
# text = 'hello world. this is a great day!'
# text = list(text)
# text = [c for c in text if c not in string.punctuation + string.whitespace]
# print(''.join(text))









# Problem 1
# Write a comprehension to generate the first 10 powers of two.
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


# nums = [2**x for x in range(10)]
# print(nums)



# Problem 2
# Write a comprehension to generate the first 10 even numbers.
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# n_nums = 11
# nums = [x for x in range(2, 2*n_nums+1, 2)]
# print(nums)





# Problem 3
# Write a dictionary comprehension to swap keys and values of a given dictionary. So {'a': 1, 'b': 2} would become {1: 'a', 2: 'b'}.


fruits = ['apples', 'banaananas', 'pears']
prices = [1.0, 0.5, 2.0]
print({fruits[i]:prices[i] for i in range(len(fruits))})

d = {'a': 1, 'b': 2}
d_flipped = {d[key]: key for key in d}
print(d_flipped)


# Problem 4
# Write a dictionary comprehension to print each letter of the alphabet and its correstponding ASCII code (check out ord)
# {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, ...}

letter_codes = {char:ord(char) for char in string.ascii_lowercase}
print(letter_codes)


