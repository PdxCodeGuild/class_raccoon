'''
Lab 24: Computer Science - Algorithms

Version 2 - Binary Search
'''


def binary_search(nums, value):
    L = 0
    R = (len(nums) - 1)
    while L <= R:
        m = (L + R)//2
        if nums[m] < value:
            L = m + 1
        elif nums[m] > value:
            R = m -1
        else:
            return m
    return -1

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(nums, 3)
print(index) # 2