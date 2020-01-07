#Compsci algorithms

import random 

def linear_search(num_list,user):
    for i in range(len(num_list)):
        if num_list[i] == user:
            return i
    return "Not found"

def binary_search(num_list,user):
    low = 0
    high = len(num_list) - 1
    
    while low <= high:
        middle = (low + high)// 2 
        if num_list[middle] < user:
            low = middle + 1
        elif num_list[middle] > user:
            high = middle - 1
        else:
            return middle
    return "Not found"

def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                sorted = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = sorted
    return nums
    
    
    
            
        


#creates a list of numbers
num_list = list(range(1,11))
#Allows the user to chose which i to find
user = input("What number do you want to find?\n:")
user = int(user)
#Runs the program with the user input and locates the i
index = linear_search(num_list,user)
binary = binary_search(num_list,user)
print(num_list)
print(f"The linear search result it {index} and the binary is {binary}")
#Bubble sort program
bubble_list = [random.randint(0,10) for i in range (10)]
print(bubble_list)
print(bubble_sort(bubble_list))
