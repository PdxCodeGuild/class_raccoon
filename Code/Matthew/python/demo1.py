


s = ''
for i in range(10):
    print(s)
    s = str(i) + ' ' + s
print(s)






exit()



# subscription and len
s = 'hello'
print(s[0]) # h
print(len(s)) # 5

# concatenation
print('hello ' + 'world')

s = 'hello'
s += ' '
s += 'world'
print(s)








print(ord('h'))
print(chr(104))






# age = input('please enter your age: ')
# age = int(age)
age = int(input('please enter your age: '))
age += 1
print(f'In 1 year you will be {age} years old!')








print(3/2)
print(3//2)


print(5%100) # 5
print(100%5) # 0
print(32%3) # 2


print(2**10) # 1024





# fruits = ['apples', 'bananas', 'pears']
# for i in range(10):
#     # print(fruits[i%len(fruits)])
#     print(f'{i}%{len(fruits)}={i%len(fruits)}')



exit()



# default
print('hello')
print('hello', sep=' ', end='\n')


print('hello', 5, 'world')
print('hello', 5, 'world', sep='')
print('hello', end=' ')
print('world')



name = input('what is your name? ')
name.isdigit() # true if name only contains 0-9, doesn't cover negative numbers
# if '5' in name:
    


