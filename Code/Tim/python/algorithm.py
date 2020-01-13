

search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def linear_search(list, num):
    index_counter = 0
    for i in range(len(list)):
        if list[i] == num:
            return i
        else:
            index_counter += 1

# lin_test = linear_search(search_list, 4)
# print(lin_test)


def bin_search(list1, num):
    low = list1[0]
    high = list1[len(list1)-1]
    mid = list1[high//2]

    while num != mid:
        if num > high or num < low:
            print('number not in range.')
            break
        for i in range(len(list1)):
            if num == low:
                return '0'
            elif num == high:
                return list1.index(high)
            elif num == mid:
                return list1.index(mid)
            elif num < mid:
                high = mid
            elif num > mid:
                low = mid


    print(low, high, mid)
    print(mid)

test = bin_search(search_list, 4)
print(test)
