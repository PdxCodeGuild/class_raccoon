

import random


def peaks(data):
    peaks_list = []
    for i in range(1, len(data)-1):
        # if i == 0 or i == len(data)-1:
        #     continue
        left = data[i-1]
        center = data[i]
        right = data[i+1]
        # if left < center and right < center:
        if left < center > right:
            peaks_list.append(i)
    return peaks_list


def valleys(data):
    valleys_list = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        center = data[i]
        right = data[i+1]
        if left > center < right:
            valleys_list.append(i)
    return valleys_list

def peaks_and_valleys(data):
    peaks_list = peaks(data)
    valleys_list = valleys(data)
    peaks_list.extend(valleys_list)
    peaks_list.sort()
    return peaks_list


def print_data(data):
    # for num in data:
    #     print('x'*num)

    max_value = max(data)
    for row in range(max_value, 0, -1):
        for col in range(len(data)):
            if data[col] < row:
                print(' ', end=' ')
            else:
                print('x', end=' ')
        print()


def generate_data1(n, min_value, max_value):
    data = []
    for num in range(n):
        data.append(random.randint(min_value, max_value))
    return data

def generate_data2(n, min_value, max_value):
    data = [random.randint(min_value, max_value)]
    for i in range(n-1):
        v = data[i] + random.randint(-1, 1)
        if v >= min_value or v <= max_value:
            data.append(v)
        else:
            data.append(data[i])
    return data

def generate_data3(n, min_value, max_value):
    data = [random.randint(min_value, max_value)]
    for i in range(n-1):
        v = data[i] + random.randint(-1, 1)
        while v < min_value:
            v = data[i] + random.randint(-1, 1)
        while v > max_value:
            v = data[i] + random.randint(-1, 1)
        data.append(v)
        # if v >= min_value or v <= max_value:
        #     data.append(v)
        # else:
        #     data.append(data[i])
    return data

def generate_data4(n, min_value, max_value):
    data = [random.randint(min_value, max_value)]
    average = (max_value + min_value)/2
    for i in range(n-1):
        v = data[i]
        if v < average:
            v += random.choice([-1, 0, 0, 1, 1, 1, 1])
        elif v > average:
            v += random.choice([-1, -1, -1, -1, 0, 0, 1])
        else:
            v += random.choice([-1, 0, 1])
        data.append(v)
    return data

# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
data = generate_data4(40, 0, 12)
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
print_data(data)
