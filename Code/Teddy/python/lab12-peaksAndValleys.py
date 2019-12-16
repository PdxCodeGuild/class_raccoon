# Lab 12: Peaks and Valleys
'''
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
'''

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

# list of data
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]



# Function call
main()

print(f'Peaks data = {peaks(data)}')

print(f'Valleys data = {valleys(data)}')
# peaks()
