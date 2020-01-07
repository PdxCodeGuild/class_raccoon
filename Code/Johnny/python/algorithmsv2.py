
def linear_search(nums, value):
    # run through a loop to find if number matches
    for i in range(len(nums)):
        # if found, returns index location of matching
        if nums[i] == value:
            return i
    else:
            print('Error not found.')


nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(f'Found at index: {index}') # 2
