'''
Filename: peaks_and_valleys.py
Author: Dylan
Purpose: Identify peak/valley locations in a list
'''

#given a list, identify all peaks and all valleys

def peaks(list):
    peak_list = []
    for i in range(1,len(list)-1):
        prev_pos = i-1
        pos = i
        next_pos = i + 1
        if list[prev_pos] < list[pos] and list[pos] > list[next_pos]:
            peak_list.append(i)
    return peak_list

def valleys(list):
    valley_list = []
    for i in range(1,len(list)-1):
        prev_pos = i-1
        pos = i
        next_pos = i + 1
        if list[prev_pos] > list[pos] and list[pos] < list[next_pos]:
            valley_list.append(i)
    return valley_list

def peaks_and_valleys(list):
    peaks_list = peaks(list)
    valleys_list = valleys(list)
    combined_list = []
    for num in peaks_list:
        combined_list.append(num)
    for num in valleys_list:
        combined_list.append(num)
    combined_list.sort()
    return combined_list

#to draw the map of x's we have to print spaces, which are hopefully equal sized
#then do if list[i] is >= whatever iteration we are on. so loop_number, or something

def draw_x(list):
    loop_number = 0
    biggest_num_in_list = max(list)
    while loop_number < biggest_num_in_list:
        for num in list:
            if num >= biggest_num_in_list - loop_number:
                print("X", end = " ")
            else:
                print(" ", end = " ")
        print()
        loop_number += 1
    return list
'''
#in this situation, I need the last index to also be counted as a peak of sorts, because water will collect beneath it. 
def lakes(list,peak_list):
    lake_list = []
    for i in range(len(peak_list) - 1):
        lake_list.append((peak_list[i],peak_list[i+1]))
    print(lake_list)
    


#we collect water between peaks. 
#so there must be two peaks between which to collect the water 
def water_collection(list):
    peak_list = peaks(list)
    lake_list = lakes(list,peak_list)
'''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

print(draw_x(data))