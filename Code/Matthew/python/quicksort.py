

'''
algorithm quicksort(A) is
    quicksort_recursive(A, 0, length(A) - 1)

algorithm quicksort_recursive(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort_recursive(A, lo, p)
        quicksort_recursive(A, p + 1, hi)

algorithm partition(A, lo, hi) is
    pivot := A[lo + (hi - lo) / 2]
    i := lo - 1
    j := hi + 1
    loop forever
        do
            i := i + 1
        while A[i] < pivot
        do
            j := j - 1
        while A[j] > pivot
        if i ≥ j then
            return j
        swap A[i] with A[j]
'''


def quicksort(nums):
    quicksort_recursive(nums, 0, len(nums)-1)

def quicksort_recursive(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quicksort_recursive(nums, low, p)
        quicksort_recursive(nums, p+1, high)

def partition(nums, low, high):
    pivot = nums[low + (high-low)//2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

import random
nums = [random.randint(0,5) for i in range(10)]
print(nums)
quicksort(nums)
print(nums)