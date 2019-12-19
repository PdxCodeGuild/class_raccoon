'''*not complete*
Peaks and Valleys

Version 3 (optional)

Make a function that takes in the dataset and a list of peaks, and returns a list of tuples representing lakes. Each tuple should have a starting x coordinate, an ending x coordinate, and a height. The height is relative to the base of the graph.

'''



#first i have to make the lists for the peaks and the valleys.

def peaks(list): #creating the loop that will define what the peaks are
    peaks_list = [] #empty because its to be defined below
    for i in range(1,len(list)-1):#for any indicy in the range of the len() or whole list to the last number (-1)
        previous_position = i-1
        position = i
        next_position = i + 1
        #this creates the peak by comparing it to the indicies on both sides and make sure they're both less
        if list[previous_position] < list[position] and list[position] > list[next_position]:
            peaks_list.append(i) #if list position is a peak then append the position to the list of peaks

    return peaks_list #this is the definition of the peaks(list). What we were looking for. So now we are returning it



def valleys(list): #creating the loop that will define what the valleys are
    valleys_list = [] #we are creating the variable to represent the valleys to be returned at the end
    for i in range(1,len(list)-1): #for any indicy in the range of the len() or whole list to the last number (-1)
        previous_position = i-1
        position = i
        next_position = i + 1
        #this creates the valley by comparing it to the indicies on both sides and make sure they're both higher
        if list[previous_position] > list[position] and list[position] < list[next_position]:
            valleys_list.append(i) #if the list position is a valley then append the position to the list of valleys

    return valleys_list #returning the list of valleys. The definition of this list


#now that those ^ functions work, I can add them together into a list of both  peaks and valleys. Basically the same thing as before

def peaks_and_valleys(list): #let's define the combo of both lists

    #these are the 3 obvious variables i need
    peaks_list = peaks(list)
    valleys_list = valleys(list)
    peaksnvalleys_list = []

    #now we're appending the peaks and valleys into the new list
    for i in peaks_list:
        peaksnvalleys_list.append(i)
    for num in valleys_list:
        peaksnvalleys_list.append(i)

    peaksnvalleys_list.sort() #sorted them

    return peaksnvalleys_list #returned the definition of the peaks and valleys list.


#this is the list of data.
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

'''
for value in data:
    print('x'*value)

^ before the graph gets turned around
'''

counter = max(data)#max of the data1 which is the height
mountain = ''#to be defined below with the while loop. variable representing the print
while counter > 0: #going through the list for each index of data1
    for value in data: #giving a value to each counter
        if value < counter:
            mountain += "   "
        else:
            mountain += "X  "
    counter -= 1 #because we are working down
    mountain += '\n'#after the loop runs for each index point it goes down a line. forms a graph

print(mountain)
print(data)
