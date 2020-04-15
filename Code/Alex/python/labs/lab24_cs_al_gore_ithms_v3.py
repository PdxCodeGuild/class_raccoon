'''
Lab 24: Computer Science - Algorithms

Version 3 - Bubble Sort
'''


def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapped = True
                print(nums)

nums = [5, 4, 3, 2, 1, 0]
bubble_sort(nums)
print(nums)