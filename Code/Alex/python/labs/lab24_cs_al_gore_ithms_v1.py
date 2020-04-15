'''
Lab 24: Computer Science - Algorithms
'''



def linear_search(nums, value):
  for i in range(len(nums)):
      if nums[i] == value:
          return i
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2