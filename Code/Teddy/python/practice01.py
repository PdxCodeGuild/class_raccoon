'''Practice 1: Fundamentals

For each practice problem, write a function that returns a value (not just prints it).
You can then call the function a couple times to test it, comment those calls out,
and move on to the next problem. An example of this format is given below.

def add(a, b):
    return a + b
print(add(5, 2))
print(add(8, 1))
'''
#**********************************************************************

'''Problem 1'''
# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)
'''
def is_even(a):
    return a%2 == 0:

print(is_even(5)) # False
print(is_even(6)) # True
'''
#**********************************************************************

'''Problem 2'''
# Write a function that takes two integers, a and b, and returns True if one is positive and the other is negative, and return False otherwise.
'''
def opposite(a, b):
    if (a > 0 and b < 0) or (a < 0 and b > 0):
        return True
    else: return False

print(opposite(10, -1)) # True
print(opposite(2, 3)) # False
print(opposite(-1, -1)) # False
'''
#**********************************************************************

'''Problem 3'''
# Write a function that returns True if a number within 10 of 100.
'''
def near_100(num):
    if num in range(90, 110):
        return True
    else:
        return False

print(near_100(50)) # False
print(near_100(99)) # True
print(near_100(105)) # True
'''
#**********************************************************************

'''Problem 4'''
# Write a function that returns the maximum of 3 parameters.
'''
def maximum_of_three(a, b, c):
    max = a
    max_list = list((a,b,c))
    for i in max_list:
        if i > max:
            max = i
    return max


print(maximum_of_three(5,6,2)) # 6
print(maximum_of_three(-4,3,10)) # 10


'''

'''
def maximum_of_three(a, b, c):
    max_list = list((a,b,c))
    max_list.sort()
    return max_list[-1]


print(maximum_of_three(5,6,2)) # 6
print(maximum_of_three(-4,3,10)) # 10
'''

#**********************************************************************

'''Problem 5'''

# Write a loop to print the powers of 2 from 2^0 to 2^20
'''
def print_powers_2():
  for exp in range(20):
      print (2 ** exp)

print_powers_2() # 1, 2, 4, 8, 16, 32, ...
'''
