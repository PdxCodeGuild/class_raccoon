# *******************************************************
# *****************    LINEAR SEARCH    *****************
# *******************************************************

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def linear_search(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i

index = linear_search(nums, 6)
print(index)

# *******************************************************
# *****************    BINARY SEARCH    *****************
# *******************************************************

def binary_search(nums, value):
    left = 0
    right = len(nums) - 1
    while left < right:
        middle = (left + right) // 2
        if nums[middle] < value:
            left = middle + 1
        elif nums[middle] > value:
            right = middle - 1
        else:
            return middle


index = binary_search(nums, 7)
print(index) 
