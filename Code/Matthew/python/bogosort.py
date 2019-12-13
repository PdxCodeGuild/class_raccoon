import random
import time

def random_list(n):
    nums = [] #choize
    for number in range(n):
        nums.append(random.randint(0,100))
    return nums


def shuffle(nums):
    # i = random.randint(0,len(nums)-1)
    # j = random.randint(0,len(nums)-1)
    # nums[i], nums[j] = nums[j], nums[i]
    for i in range(len(nums)):
        j = random.randint(0,len(nums)-1)
        nums[i], nums[j] = nums[j], nums[i]


def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True


def get_time():
    return int(round(time.time() * 1000))

def bogosort(nums):
    steps = 0
    start_time = get_time()
    while is_sorted(nums) == False:
        shuffle(nums)
        steps += 1

    end_time = get_time()
    time_taken = end_time - start_time
    print(f'total time taken: {time_taken/1000} seconds')
    print(f'time per step:    {time_taken/1000/steps} seconds')
    print(f'steps:            {steps}')






nums = random_list(8)
print(nums)
bogosort(nums)
print(nums)


#mobrulerules
