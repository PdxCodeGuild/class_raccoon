
# import random
#
# input('Pick a number between 1 and 10...')
# while True:
#     num = random.randint(1, 10)
#     answer = input(f'Is it {num}? ').lower()
#     if answer in ['y', 'yes']:
#         print(f'your number was {num}')
#         break



# input('Pick a number between 1 and 10...')
# for num in range(1,11):
#     answer = input(f'Is it {num}? ').lower()
#     if answer in ['y', 'yes']:
#         print(f'your number was {num}')
#         break


input('Pick a number between 1 and 100...')
lower = 1
upper = 100
while True:
    num = (lower + upper) // 2
    answer = input(f'Is it {num}? ').lower()
    if answer in ['y', 'yes']:
        print(f'your number was {num}')
        break
    answer = input(f'Is your number higher or lower than {num}? ').lower()
    if answer == 'higher':
        lower = num
    else:
        upper = num
