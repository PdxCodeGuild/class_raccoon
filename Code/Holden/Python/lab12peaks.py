datastart = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 8, 6, 7, 8, 9, 8, 7]
def pvfind(data):
    peaksout=[]
    valleysout=[]
    for i in range(len(data)):
        if i==0 and data[i] > data[i+1]:
            peaksout.append(i)
            continue
        if i==0 and data[i] < data[i+1]:
            valleysout.append(i)
            continue
        if i==len(data)-1 and data[i-1] < data[i]:
            peaksout.append(i)
            continue
        if i==len(data)-1 and data[i-1] > data[i]:
            valleysout.append(i)
            continue
        if data[i]<data[i+1] and data[i]<data[i-1]:
            valleysout.append(i)
            continue
        if data[i]>data[i+1] and data[i]>data[i-1]:
            peaksout.append(i)
            continue
    return peaksout, valleysout
print(pvfind(datastart))
loop = 0
while loop < max(datastart):
    for h in datastart:
        if h < max(datastart)-loop:
            print(" ", end=" ")
        else:
            print("X", end=" ")
    print("")
    loop += 1
water = 0
while True:
    prevwater = water
    peaks = pvfind(datastart)[0]
    print(peaks)
    for i in range(len(peaks)-1):
        highest_peak = -1
        for j in range(i+1, len(peaks)):
            if highest_peak == -1:
                highest_peak = peaks[j]
            if datastart[highest_peak] < datastart[peaks[j]]:
                highest_peak = peaks[j]
        if len(peaks)-1 == i+1:
            highest_peak = peaks[i+1]
        print(f"{highest_peak} highest")
        if peaks[i] <= datastart[highest_peak]:
            for pk in range(peaks[i]+1, highest_peak+1):
                print(f"{pk} height")
                if datastart[peaks[i]] > datastart[pk]:
                    water += datastart[peaks[i]] - datastart[pk]
                    datastart[pk] = datastart[peaks[i]]
    if prevwater == water:
        break
    datastart.reverse()


print(f"The valleys in this range can hold {water} units of water.")
