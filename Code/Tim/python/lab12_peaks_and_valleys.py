data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8]

def valley(x):
    for num in range(len(x)):
        if num == len(x)-1:
            break
        if x[num-1] > x[num] and x[num+1] > x[num]:
            print(x[num])

def peak(x):
    for num in range(len(x)):
        if num == len(x)-1:
            break
        if x[num-1] < x[num] and x[num+1] < x[num]:
            print(x[num])

def graph(x):
    line = max(x)
    while line >= 0:
        # for num in x:
            for position in range(len(x)):
                if x[position] <= line:
                    print((' ' * x[position])+'x'*line)
            line = line - 1



valley(data)
peak(data)
graph(data)
