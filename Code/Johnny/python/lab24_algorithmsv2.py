def binary_search(nums, value):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high)//2
        if value > nums[mid]:
            low = mid + 1
        elif value < nums[mid]:
            high = mid - 1
        else:
            return mid
    return


nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(nums)
index = binary_search(nums, 4)
print(index) # 2
