data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peak_list = []
valley_list = []
both_list = []
def pv_decider(data):
    for i in range(len(data)):
      
        if i == len(data) - 1:
            return
        elif i - 1 < 0:
            continue
        point1 = (data[i+1])
        point2 = (data[i-1])
        if point1 == point2:
            point3 = data[i]
            if point1 < point3:
                peak_list.append(i)
                both_list.append(i)
            elif point1 > point3:
                valley_list.append(i)
                both_list.append(i)
    return peak_list, valley_list
pv_decider(data)
print(f"The peaks are{peak_list}and the valleys are {valley_list} and together they are {both_list}")

def pv_draw(data):
    mountainview = ""
    maxpoint = max(data)
    while maxpoint > 0:
        for i in data:
            if i > maxpoint:
                mountainview += (" X ")
            else: 
                mountainview += ("   ")
        maxpoint = maxpoint-1
        mountainview += "\n" 
    return mountainview   
print(pv_draw(data))