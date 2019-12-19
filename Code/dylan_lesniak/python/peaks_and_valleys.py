'''
Filename: peaks_and_valleys.py
Author: Dylan
Purpose: Identify peak/valley locations in a list
'''

#mods
import numpy as np
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
        print("", end = " ")
        for num in list:
            if num >= biggest_num_in_list - loop_number:
                print("X ", end = " ")
            else:
                print("  ", end = " ")
        print()
        loop_number += 1
    return list

#in this situation, I need the last index to also be counted as a peak of sorts, because water will collect beneath it. 
#what I should do is make a modified peak list. 
#the only two things that need to be checked for are the first and last positions
#so if list[0] > list[1], add the index, and if list[-1] > list[-2], add the index to the peak list. OK break. 
def high_points(list,peaks,valleys):
    p_and_v = peaks
    p_and_v.extend(valleys)
    p_and_v.sort()
    return p_and_v
    
#we have our high points. From here, a lake will be the the one equal the the lowest peak of the pair.
#you have to go from first peak until you get to an identical height. 
#then, you just get a list of water nums, 
#gonna do it Matthew's way. Go through each row at the top. 
#Maybe start just by going 
def lakes(data,high_points):
    

    return count
      
    
def flatten(data):
    flattened_list = []
    for ele in data:
        if type(ele) != list:
            flattened_list.append(ele)
        else:
            flattened_list.extend(flatten(ele))
    return flattened_list

#we collect water between peaks. 
#so there must be two peaks between which to collect the water 
def water_collection(list):
    peak_list = peaks(list)
    high_points = high_points(list,peaks(list),valleys(list))
    lakes = lakes(list,high_points)



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 4, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(draw_x(data))
idx = []
for i in range(len(data)):
    idx.append(i)
print (idx)

peak_list = peaks(data)
valley_list = valleys(data)
high_point_list = high_points(data,peak_list,valley_list)
print(lakes(data,high_point_list))