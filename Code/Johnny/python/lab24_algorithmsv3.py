def bubble_sort(nums):
    for num in range(len(nums)-1,0,-1):
        for i in range(num):
            if nums[i]>nums[i+1]:
                templist = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = templist
                print(nums)


nums = [5, 4, 3, 2, 1, 0]
bubble_sort(nums)
print(nums)
