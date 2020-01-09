

import time
import random

# // A - the list
# // n - the length of the list
# // T - the value we're searching for
# function binary_search(A, n, T) is
#     L := 0
#     R := n − 1
#     while L ≤ R do
#         m := floor((L + R) / 2)
#         if A[m] < T then
#             L := m + 1
#         else if A[m] > T then
#             R := m - 1
#         else:
#             return m
#     return unsuccessful


def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return None

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        m = (low + high) // 2
        if nums[m] < target:
            low = m + 1
        elif nums[m] > target:
            high = m - 1
        else:
            return m
    return None




# start_time = time.time()
# nums = [random.randint(0,99) for i in range(100000)]
# nums.sort()
# for i in range(1000):
#     index = random.randint(0, len(nums)-1)
#     index = linear_search(nums, nums[index])
# end_time = time.time()
# print(end_time - start_time)
#
#
# start_time = time.time()
# nums = [random.randint(0,99) for i in range(100000)]
# nums.sort()
# for i in range(1000):
#     index = random.randint(0, len(nums)-1)
#     index = binary_search(nums, nums[index])
# end_time = time.time()
# print(end_time - start_time)






# procedure bubbleSort(A : list of sortable items)
#     n := length(A)
#     repeat
#         swapped = false
#         for i := 1 to n - 1 inclusive do
#             /* if this pair is out of order */
#             if A[i - 1] > A[i] then
#                 /* swap them and remember something changed */
#                 swap(A[i - 1], A[i])
#                 swapped := true
#             end if
#         end for
#     until not swapped
# end procedure


def bubble_sort(nums):
    n = len(nums)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]

                # t = nums[i]
                # nums[i] = nums[i-1]
                # nums[i-1] = t

                swapped = True



# i ← 1
# while i < length(A)
#     j ← i
#     while j > 0 and A[j-1] > A[j]
#         swap A[j] and A[j-1]
#         j ← j - 1
#     end while
#     i ← i + 1
# end while

def insertion_sort(nums):
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
        i += 1




# algorithm quicksort(A) is
#     quicksort_recursive(A, 0, length(A) - 1)
#
# algorithm quicksort_recursive(A, lo, hi) is
#     if lo < hi then
#         p := partition(A, lo, hi)
#         quicksort_recursive(A, lo, p)
#         quicksort_recursive(A, p + 1, hi)
#
# algorithm partition(A, lo, hi) is
#     pivot := A[lo + (hi - lo) / 2]
#     i := lo - 1
#     j := hi + 1
#     loop forever
#         do
#             i := i + 1
#         while A[i] < pivot
#         do
#             j := j - 1
#         while A[j] > pivot
#         if i ≥ j then
#             return j
#         swap A[i] with A[j]



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


from time import sleep
from threading import Timer

def sleepsort(values):
    sleepsort.result = []
    def add1(x):
        sleepsort.result.append(x)
    mx = values[0]
    for v in values:
        if mx < v: mx = v
        Timer(v, add1, [v]).start()
    sleep(mx+1)
    return sleepsort.result





def test_sort_algorithm(sort_algorithm):
    start_time = time.time()
    for i in range(1000):
        nums = [random.randint(0,99) for i in range(1000)]
        sort_algorithm(nums)
    end_time = time.time()
    print(end_time - start_time)




test_sort_algorithm(bubble_sort)
test_sort_algorithm(insertion_sort)
test_sort_algorithm(insertion_sort)

