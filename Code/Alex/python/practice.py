def add(a, b):
    return a + b
#print(add(5, 2))
#print(add(8, 1))



def is_even(a):
    #a = 5
    a//2 # 2
    a/2 # 2.5
    a%2 # 1

    #a = 6
    a//2 # 3
    a/2 # 3
    a%2 # 0



    if a%2 == 0:
        return True
    else:
        return False



result = is_even(5)
if is_even(5):
    print('is even')
    print('is odd')
print(is_even(5)) # False
print(is_even(6))  # True
