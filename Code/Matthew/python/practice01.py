



# def add(a, b, c):
#     return a + b
#     print(add(5, 2))
# print(add(8, 1))
# print(add(8))

# age = input('what is your age? ')
# age = 45
# print(add(age, 1))



def is_even(a):
    
    # a = 5
    # a//2 # 2
    # a/2 # 2.5
    # a%2 # 1
    # 
    # a = 6
    # a//2 # 3
    # a/2 # 3
    # a%2 # 0
    
    # if a%2 == 0:
    #     return True
    # else:
    #     return False
    # 
    # if a%2 == 0:
    #     return True
    # return False
    
    return a%2 == 0
    

# result = is_even(5)
# if is_even(5):
#     print('is even')
# else:
#     print('is odd')
# print(is_even(5)) # False
# print(is_even(6)) #True



def opposite(a, b):
    # if (a < 0 and b > 0) or (a > 0 and b < 0):
    #     return True
    # if a*b < 0:
    #     return True
    # else:
    #     return False
    return a*b < 0
# print(opposite(10, -1)) # True
# print(opposite(2, 3)) # False
# print(opposite(-1, -1)) # False



# Problem 3
# Write a function that returns True if a number within 10 of 100.

def near_100(num):
    return num > 90 and num < 110
    
    # if num in range(90, 110):
    #     return True
    # else:
    #     return False
    
# print(near_100(50)) # False
# print(near_100(99)) # True
# print(near_100(105)) # True


# Problem 4
# Write a function that returns the maximum of 3 parameters.
def maximum_of_three(a, b, c):
    
    # nums = [a, b, c]
    # nums.sort()
    # return nums[2]
    
    # max = 0
    # max = -9999999
    # max = float('-inf')
    max = a
    # if a > max:
    #     max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max
    
    # if a > b:
    #     if a > c:
    #         return a
    #     elif c > b:
    #         return c
    #     else:
    #         return b
    # elif b > c:
    #     return b
    # else:
    #     return c
    
    
    
# print(maximum_of_three(5, 6, 2)) # 6
# print(maximum_of_three(-4, 3, 10)) # 10
# print(maximum_of_three(-4, -3, -10)) # -3




# Problem 5
# Print out the powers of 2 from 2^0 to 2^20


for x in range(21):
    print(x, 2**x)



def min(a, b):
    if a < b:
        return a
    return b
    





