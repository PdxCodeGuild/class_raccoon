# Lab 12: Peaks and Valleys
import random

'''
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
'''

'''
# Version 1
# printing x function
#  Main function call
def main():
    for i in data:
       print(i, ('x' * i) )

# Finding peak function
def peaks(data):
    output = []
    for i in range(len(data)):
        if i == len(data) - 1:
            break
        if data[i] > data[i - 1] and data[i] > (data[i + 1]):
            output.append(data[i])
    return output

# Finding valley function
def valleys(data):
    output = []
    for i in range(len(data)):
        if i == len(data) - 1:
            break
        if data[i] < data[i-1] and data[i] < data[i+1]:
            output.append(data[i])
    return output

def peaks_valleys(data):
    peal_list

# list of data
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]



# Function call
main()

print(f'Peaks data = {peaks(data)}')

print(f'Valleys data = {valleys(data)}')
'''


# version 2

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


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# data = generate_data4(40, 0, 12)
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
print_data(data)
