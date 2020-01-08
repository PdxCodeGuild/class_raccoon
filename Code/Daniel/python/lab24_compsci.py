#linear list search
def linear_search(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i

nums = [1, 2, 3, 4, 5, 6, 7, 8]
lin_search = linear_search(nums, 3)



def binary_search(nums, value):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < value:
            low = mid + 1
        elif nums[mid] > value:
            high = mid - 1
        else:
            return mid
    return("No dice")

nums = [1, 2, 3, 4, 5, 6, 7, 8]
bin_search = binary_search(nums, 3)


def bubble_sort(nums):
    lengh = len(nums) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(lengh):
            if nums[i] > nums[i+1]:
                sorted = False
                nums[i],nums[i+1] = nums[i+1], nums[i]
    return nums

nums = [2, 3, 5, 4, 6, 9, 7, 8, 1]
bub_sort = bubble_sort(nums)



def insert_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j],  nums[j-1]
            j-=1
    return nums

nums = [2, 3, 5, 4, 6, 9, 7, 8, 1]
in_sort = insert_sort(nums) 


print(f"Linear search result is {lin_search}, binary search result is {bin_search}, bubble sort results are {bub_sort}, and insert sort results are {in_sort}")