def insertion_sort(nums):
   for i in range(1,len(nums)):

     current = nums[i]
     pos = i

     while pos>0 and nums[pos-1]>current:
         nums[pos]=nums[pos-1]
         pos = pos-1

     nums[pos]=current
     print(nums)

nums = [6,7,8,9,3,4,2,1,5,0]
insertion_sort(nums)
print(nums)
