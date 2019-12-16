# lab18_peaks_and_valleys.py
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# define element in data list, returns index position
print(data)
peak = []
valley = []
both = []
# for loop to iteriate through elements
for i in range(1, len(data)-1):
    if data[i] > data[i-1] and data[i] > data[i+1]:
        # append to index
        peak.append(i)
        both.append(i)
    elif data[i] < data[i-1] and data[i] < data[i+1]:
        valley.append(i)
        both.append(i)
print(f"Peak: {peak} ")
print(f"Valley: {valley} ")
print(f"Peaks & Valleys: {both} ")

# function to loop through data elements
def sideways(data):
    mountain = ""
    maxpoint = max(data)
    while maxpoint > 0:
        for i in data:
            if i + 1 > maxpoint:
                mountain += (" X ")
            else:
                mountain += ("   ")
        maxpoint = maxpoint-1
        mountain += "\n"
    return mountain
print(sideways(data))
print(data)
