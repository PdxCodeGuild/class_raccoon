


def is_even(num):
    return num%2 == 0


def eveneven(nums):
    even_numbers = 0
    for num in nums:
        if is_even(num):
            even_numbers += 1
    return is_even(even_numbers)


# print(eveneven([5, 6, 2])) # True
# print(eveneven([5, 5, 2])) # False
# print(eveneven([5, 5, 2, 2, 3, 2, 1, 4])) # True



def print_every_other_while(nums):
    i = 0
    while i < len(nums):
        print(nums[i])
        i += 2

def print_every_other_for(nums):
    for i in range(0, len(nums), 2):
        print(nums[i])

# print_every_other_while([0, 1, 2, 3, 4, 5, 6, 7, 8]) # 0, 2, 4, 6, 8
# print_every_other_for([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) # 0, 2, 4, 6, 8




def extract_less_than_ten(nums):
    output = []
    for i in range(len(nums)):
        if nums[i] < 10:
            # print(nums[i])
            output.append(nums[i])
    return output
# print(extract_less_than_ten([2, 8, 12, 18, 5, 6, 7, 8, 12, 100])) # [2, 8]





def common_elements(nums1, nums2):
    output = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                output.append(nums1[i])
    return output
# print(common_elements([1, 2, 3], [2, 3, 4])) # [2, 3]



# Problem 10
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

def merge(nums1, nums2):
    merged = []
    for i in range(len(nums1)):
        merged.append([nums1[i], nums2[i]])
    return merged
# print(merge([5,2,1], [6,8,2])) # [[5,6],[2,8],[1,2]]



# Problem 13
# Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.


def minimum(nums):

    # bogosort.bogosort(nums)
    # nums.sort()
    # return nums[0]

    running_minimum = nums[0] # float('inf')
    for num in nums:
        if num < running_minimum:
            running_minimum = num
    return running_minimum




def maximum(nums):
    running_maximum = nums[0] # float('-inf')
    for num in nums:
        if num > running_maximum:
            running_maximum = num
    return running_maximum



def mean(nums):
    running_total = 0
    for num in nums:
        running_total += num
    return running_total / len(nums)




nums = [1, 2, 3, 4, 5, 6]
print(minimum(nums))
print(maximum(nums))
print(mean(nums))
