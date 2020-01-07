def insertion_sort(nums):
   for index in range(1,len(nums)):

     currentvalue = nums[index]
     position = index

     while position>0 and nums[position-1]>currentvalue:
         nums[position]=nums[position-1]
         position = position-1

     nums[position]=currentvalue
     print(nums)

nums = [6,7,8,9,3,4,2,1,5,0]
insertion_sort(nums)
print(nums)
