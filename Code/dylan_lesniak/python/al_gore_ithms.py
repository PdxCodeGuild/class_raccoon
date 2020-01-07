'''
Filename: al_gore_ithms.py
Author: Dylan
Purpose: Practice algorithms
'''

#VERSION 1:
def linear_search(nums, value):
    i = 0 
    for i in range(len(nums)):
        if nums[i] == value:
            return i 
    return "ERROR: VALUE NOT FOUND"

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 50000)
# print(index) # 2

#VERSION 2:
def binary_search(nums, value): 
    temp_list = nums
    i = 0 
    while len(temp_list) > 1: 
        halfway_point = len(temp_list)//2
        halfway_value = temp_list[halfway_point]
        if halfway_value == value:
            i += halfway_point
            return i 
        elif halfway_value < value:
            i += halfway_point
            temp_list = temp_list[halfway_point:]
        elif halfway_value > value:
            temp_list = temp_list[:halfway_point]
        else:
            return "ERROR: VALUE NOT IN RANGE"
    return "ERROR: VALUE NOT IN RANGE"

#VERSION 3:
nums = [5,1,4,2,9,8]
print(nums)

#jeez, just gotta :=
def bubble_sort(nums):
    swapped = True
    while swapped == True:
        swapped = False
        i = 0
        while i < (len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
            i += 1
    return nums

def insertion_sort(nums):
    i = 1
    while i < len(nums):
        j = i 
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
        i += 1
    return nums

#VERSION 5:
#from my understanding, splits the list in half, then sorts each half (by sorting each half recursively). 
def quicksort(nums):
    quicksort_recursive(nums,0,(len(nums)-1))

def quicksort_recursive(nums,low,high):
    if low < high: #if high and low are at least equal, then the length of unsorted values is 1, so it's sorted. BASE CASE.
        part = partition(nums,low,high)
        quicksort_recursive(nums,low,part) #sorts the first half
        quicksort_recursive(nums,part+1,high) #

def partition(nums, low, high): 
    mid = (low + high) // 2
    if nums[mid] < nums[low]:
        nums[low], nums[mid] = nums[mid], nums[low]
    elif nums[high] < nums[low]:
        nums[low],nums[high] = nums[high],nums[low]
    elif nums[mid] < nums[high]:
        nums[mid], nums[high] = nums[high], nums[mid]
    pivot = nums[high]
    i = low
    j = high
    while True:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j 
        nums[i], nums[j] = nums[j], nums[i]

quicksort(nums)
print(nums)
        
