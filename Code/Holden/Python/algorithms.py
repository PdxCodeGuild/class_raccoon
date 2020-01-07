import random
import time

def linear_search(search_list, value):
    index = 0
    for num in search_list:
        if num == value:
            return index
        index += 1
    else:
        return -1

def bin_search(sorted_list, value):
    lower = 0
    upper = len(sorted_list)-1
    while lower <= upper:
        print(lower, upper)
        mid = (upper + lower) // 2
        if sorted_list[mid] > value:
            upper = mid - 1
        elif sorted_list[mid] < value:
            lower = mid + 1
        elif sorted_list[mid] == value:
            return mid
    else:
        return -1

def bubble_sort(unsorted_list):
    sorting = True
    while sorting:
        sorting = False
        for i in range(len(unsorted_list)-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                sorting = True

def insertion_sort(unsorted):
    for i in range(1,len(unsorted)):
        if unsorted[i] < unsorted[i-1]:
            j = i
            while unsorted[i] < unsorted[j-1] and j != 0:
                j -= 1
            popped = unsorted.pop(i)
            unsorted.insert(j, popped)

def partition(unsorted, i, j):
    piv = unsorted[(j+i)//2]
    i -= 1
    j += 1
    while True:
        i += 1
        while unsorted[i] < piv:
            i += 1
        j-=1
        while unsorted[j] > piv:
            j -= 1
        if i >= j:
            return j
        unsorted[i], unsorted[j] = unsorted[j], unsorted[i]


def quick_recursive(unsorted, lo, hi):
    if lo < hi:
        p = partition(unsorted, lo, hi)
        quick_recursive(unsorted, lo, p)
        quick_recursive(unsorted, p + 1, hi)


def quicksort(unsorted):
    quick_recursive(unsorted, 0, len(unsorted)-1)

def compressionsort(unsorted):
    num_values = {}
    for num in unsorted:
        if num not in num_values:
            num_values[num] = 1
        else:
            num_values[num] += 1
    sorted_list = []
    for_sort = [key for key in num_values]
    for_sort.sort()
    for key in for_sort:
        for i in range(num_values[key]):
            sorted_list.append(key)

    return sorted_list


# test = []
# for i in range(10):
#     test.append(i)
# print(bin_search(test, 10))

sorttest = []
for i in range(500000):
    sorttest.append(random.randint(1,500000))
# print(sorttest)
# bubble_sort(sorttest)
start_comp = time.time()
comp_sorted = compressionsort(sorttest)
end_comp = time.time()
sorttestq = sorttest
start_quick = time.time()
quicksort(sorttestq)
end_quick = time.time()
start_tim = time.time()
sorttest.sort()
end_tim = time.time()
# print(comp_sorted)
print(f"compressionsort took {end_comp - start_comp} seconds.")
print(f"quicksort took {end_quick-start_quick} seconds")
print(f"timsort took {end_tim-start_tim} seconds")
