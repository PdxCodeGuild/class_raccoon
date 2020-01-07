#csalgorithms.py

#Version 1 - Linear Search
def linear_search(nums, value):
    # Check if each element equal to given value
    for i in range(len(nums)):
        if nums[i] == value:
            return i
    return indexlist
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2

#Version 2 - Binary Search
def binary_search(nums, value):
    #binary list must be sorted
    nums.sort()
    #define two indices, low and high:
    low = 0
    high = len(nums) - 1
    #define third index:
    while low < high:
        if value > high or value < low:
            return "Value not found!"
        mid = (low + high) // 2
        if value == nums[mid]:
            return mid
        elif value < nums[mid]:
            high = mid
        elif value > nums[mid]:
            low = mid
        else:
            return "Value not found!"

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(nums, 3)
print(index) # 2

#Version 3 - Bubble sort
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)):
            if i > 0 and i < len(nums):
                if nums[i-1] > nums[i]:
                    nums[i],nums[i-1] = nums[i-1],nums[i]
                    swapped = True
    return nums

nums = [44, 3, 4, 3, 2, 1, 9, 13]
sort = bubble_sort(nums)
print(sort)

#Version 4 - Insertion sort
def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j],nums[j-1] = nums[j-1],nums[j]
            j -= 1
    return nums

nums = [44, 3, 4, 3, 2, 1, 9, 13]
sort = insertion_sort(nums)
print(sort)

# #Version 5 - Quicksort
# def quicksort_recursive(nums):
#     lo = []
#     hi = []
#
#
# def partition(nums):
#     pivot =
#
#
