#lab12_pnv.py

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(input):
    peaks_list = []
    for x in range(len(input)):
        if x == len(input) - 1:
            return peaks_list
        elif input[x-1] < input[x]:
                if input[x+1] == input[x-1]:
                    peaks_list.append(x)
        else:
            continue

def valleys(input):
    valleys_list = []
    for x in range(len(input)):
        if x == len(input) - 1:
            return valleys_list
        elif input[x-1] > input[x]:
                if input[x+1] == input[x-1]:
                    valleys_list.append(x)
        else:
            continue

def peaks_and_valleys(input1, input2):
    pnv_list = input1 + input2
    pnv_list.sort()
    return pnv_list

peaks_list = peaks(data)
valleys_list = valleys(data)
pnv_list = peaks_and_valleys(peaks(data), valleys(data))

print(f"The peaks are at: {peaks_list}")
print(f"The valleys are at: {valleys_list}")
print(f"The peaks and valleys are at: {pnv_list}")

# Version 2 - Draw the X's

for x in reversed(range((max(data)))):
    picture=""
    height = x+1
    for y in data:
        if y >= height:
            picture+="X "
        else:
            picture+="  "
    print(picture)

# Version 3 - Tuples
# for z in data:
#     for y in peaks_list[0]
#         if
#     print(peaks_list[0])
    # print(z)
    # if peaks_list[0] < z:
    #     print("0 ")
    # else:
    #     print("X ")
