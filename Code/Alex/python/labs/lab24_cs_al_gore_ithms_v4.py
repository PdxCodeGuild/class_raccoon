'''
Lab 24: Computer Science - Algorithms

Version 4 - Insertion Sort
'''

def insertion_sort(nums):
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
        i += 1
        print(nums)

nums = [5, 4, 3, 2, 1, 0]
insertion_sort(nums)
print(nums)