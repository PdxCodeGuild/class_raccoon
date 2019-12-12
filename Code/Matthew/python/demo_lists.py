


#             0         1          2          3        4          5          6          7
#        0         1          2        3          4          5         6           7
fruits = ['apples', 'bananas', 'pears', 'cherries', 'tomato', 'oranges', 'cucumber', 'avocado']


print(fruits[0]) # apples
print(fruits[2:4]) # pears, cherries
print(fruits[:2]) # apples, bananas
print(fruits[5:]) # oranges, cucumber, avocado
print(fruits[::2]) # apples, pears, tomato, cucumber
print(fruits[::-1]) # avocado, cucmber, oranges, ... apples


# fruits = ['apples', 'bananas', 'pears']
# print(fruits.index('hello world'))





fruits.sort()
print(type(fruits))
print('===========')
print(fruits)
print('==========')

for fruit in sorted(fruits):
    print(fruit)


fruits = ['apples', 'bananas', 'pears', 'cherries', 'pineapple']
for fruit in fruits:
    fruit += '!' # does not change original value

for i in range(len(fruits)):
    fruit = fruits[i]
    fruit += '!' # does not change original value
    
    fruits[i] += '!' # DOES change the original value in the list



nums = [5, 6, -3, 2, 4, -8, 10]
for num in nums:
    if num < 0:
        continue
    print(num)


