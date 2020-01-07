'''
Computer Science - Algorithms
Version 1 - Linear Search

Implement linear search, which simply loops through the given list and check
if each element is equal to the value we're searching for.
If it is, return the index at which it was found, otherwise,
return a value indicating that it was not found.

Example run:

 I
[1, 2, 3, 4, 5, 6, 7, 8]
    I
[1, 2, 3, 4, 5, 6, 7, 8]
       I
[1, 2, 3, 4, 5, 6, 7, 8]
Stub:

def linear_search(nums, value):
  ...

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2
'''

def linear_search(nums, value):
    for i in range(len(nums)):
        if value == nums[i]:
            return i
    return -1

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 7)
print(index) # 2
