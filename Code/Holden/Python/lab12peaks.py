data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 8, 6, 7, 8, 9, 8, 7]
peaks=[]
valleys=[]
for i in range(len(data)):
    if i==0 and data[i] > data[i+1]:
        peaks.append(i)
        continue
    if i==0 and data[i] < data[i+1]:
        valleys.append(i)
        continue
    if i==len(data)-1 and data[i-1] < data[i]:
        peaks.append(i)
        continue
    if i==len(data)-1 and data[i-1] > data[i]:
        valleys.append(i)
        continue
    if data[i]<data[i+1] and data[i]<data[i-1]:
        valleys.append(i)
        continue
    if data[i]>data[i+1] and data[i]>data[i-1]:
        peaks.append(i)
        continue
print(peaks)
print(valleys)
loop = 0
while loop < max(data):
    for h in data:
        if h < max(data)-loop:
            print(" ", end=" ")
        else:
            print("X", end=" ")
            
    outline = "".join(cross for cross in output)
    print(outline)
    loop += 1
water = 0
# for i in range(len(peaks)-1):
#     highest_peak = -1
#     for j in range(i+1, len(peaks)):
#         if highest_peak == -1:
#             highest_peak = peaks[j]
#         if data[highest_peak] < data[peaks[j]]:
#             highest_peak = peaks[j]
#     if len(peaks)-1 == i+1:
#         highest_peak = peaks[i+1]
#     print(f"{highest_peak} high")
#     if peaks[i] <= data[highest_peak]:
#         for pk in range(peaks[i]+1, highest_peak+1):
#             if data[peaks[i]] > data[pk]:
#                 water += data[peaks[i]] - data[pk]
#     else:
#         for pk in range(peaks[i]+1, highest_peak+1):
#             print(f"{pk} index")
#             if data[highest_peak] > data[pk]:
#                 print(data[pk])
#                 water += data[highest_peak] - data[pk]

print(f"The valleys in this range can hold {water} units of water.")
