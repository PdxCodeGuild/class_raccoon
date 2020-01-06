#lab21_raindata_verA.py
#analyzing a single file
import datetime
import re
import math
import matplotlib.pyplot as plt

#open file
file_path = r'../pcc_cascade.rain'

with open(file_path, 'r') as file:
    raindata = file.read()
file.close()

#get file title
filetitle = re.findall('\A.*', raindata)
filetitle = ''.join(filetitle)
#pull totals by date from file
datatup = re.findall('(\d{2}-\w{3}-\d{4})\s*(\d*)', raindata)

datatup = [x for x in datatup if x[1].isdigit() == True]

#convert data into useable format
for x in range(len(datatup)):
    date = datetime.datetime.strptime(datatup[x][0], '%d-%b-%Y')
    rainfall = (int(datatup[x][1])*.01) #converts to integer value in Inches
    datatup[x] = (date,rainfall)

#define formula for calculating mean
def mean(tuplist):
    sum = 0
    for x in tuplist:
        sum += x[1]
    calcmean = sum/len(tuplist)
    return(calcmean)

#define formula for calculating standard deviation
def std(tuplist):
    newsum = 0
    sum = mean(tuplist)
    for x in tuplist:
        newsum += (x[1] - sum)**2
    calcstd = math.sqrt(newsum/(len(tuplist) - 1))
    return(calcstd)

#calculate mean and standard deviation
meancalc = mean(datatup)
stdcalc = std(datatup)

#display results for mean and standard deviation
print(f"The mean rainfall is {round(meancalc, 2)} inches, and the standard deviation is {round(stdcalc, 2)} inches.")

#calculate percentage of results that are 1 std deviation from mean
deviant = 0
for x in datatup:
    if x[1] >= (meancalc - stdcalc) and x[1] <= (meancalc + stdcalc):
        deviant += 1
deviation = (deviant/len(datatup))*100

print(f"{round(deviation, 2)}% of the data is within 1 standard deviation of the mean.")

#find day with most rain
mostrain = max(datatup, key = lambda x: x[1])
raindates = []
for x in range(len(datatup)): #pull all dates that match the highest rainfall
    if datatup[x][1] == mostrain[1]:
        raindates.append(datatup[x])
raindates.reverse() #display in chronological order, oldest to newest

print(f"The highest amount of rainfall in a single day was {mostrain[1]} inches, which occurred on the following date(s):")
for x, y in raindates:
    print(date.strftime('%d-%b-%Y'))

#find year with most rain on average
years = []
yeartup = []
for x in range(len(datatup)): #initiate list of touples by year
    if datatup[x][0].year not in years:
        years.append(datatup[x][0].year)
        yeartup.append(tuple([datatup[x][0].year,0,0]))
for x in range(len(datatup)): #update counts with list
    for y in range(len(yeartup)):
        if datatup[x][0].year == yeartup[y][0]:
            year = datatup[x][0].year
            totalrain = datatup[x][1] + yeartup[y][1]
            daycount = yeartup[y][2] + 1
            yeartup[y] = (year, totalrain, daycount)

#get average rainfall
yearavg = []
for y in range(len(yeartup)):
    average = (yeartup[y][2] / yeartup[y][1])
    yearavg.append(tuple((yeartup[y][0], average)))

#get highest average
bigyear = max(yearavg, key = lambda x: x[1])
rainyear = []
for x in range(len(yearavg)): #pull all years that match the highest rainfall
    if yearavg[x][1] == bigyear[1]:
        rainyear.append(yearavg[x])
rainyear.reverse() #display in chronological order, oldest to newest

#display highest average:
print(f"The highest average annual rainfall was {round(bigyear[1], 2)} inches, which occurred in the following year(s):")
for x in rainyear:
    print(x[0])

#Version 3 - Create Chart of Daily Totals
def plot(x_values, y_values, title):
    plt.plot(x_values, y_values)
    plt.title(filetitle + "\n" + title)
    plt.show()

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for x in months:
    x = datetime.datetime.strptime(x, '%b')

#Create chart of daily totals for given year
year = []
for i in range(len(datatup)):
    if datatup[i][0].year not in year:
        year.append(datatup[i][0].year)
    year.sort()
while True:
    useryear = input(f"Please type in a year (from {year[0]} to {year[-1]}) to show daily totals: ")
    if useryear.isdigit():
        useryear = int(useryear)
        if useryear in year:
            break
        else:
            print("Invalid year!")
            continue
    else:
        print("Invalid entry!")
x_values = months
y_values = [0 for x in x_values]

for i in range(len(datatup)):
    if datatup[i][0].year == useryear:
        for y in range(len(x_values)):
            if datatup[i][0].strftime('%b') == x_values[y]:
                y_values[y] += datatup[i][1]
plot(x_values, y_values, f"Daily Rainfall (in Inches) for {useryear}")

#Monthly totals, average across multiple years
x2_values = months
y2_values = []
for x in x2_values:
    y2_values.append(0)
for y in range(len(datatup)):
    for z in range(len(x2_values)):
        if datatup[y][0].strftime("%b") == x2_values[z]:
            y2_values[z] += datatup[y][1]
for y in y2_values:
    y = y/(len(y2_values))

plot(x2_values, y2_values, f"Monthly Average Rainfall (in Inches) from {year[0]} to {year[-1]}")

#Total yearly rainfall, year by year
x3_values = []
y3_values = []
for x in range(len(datatup)):
    if datatup[x][0].strftime("%Y") not in x3_values:
        x3_values.append(datatup[x][0].strftime("%Y"))
        y3_values.append(0)
x3_values.sort()
for y in range(len(datatup)):
    for z in range(len(x3_values)):
        if datatup[y][0].strftime("%Y") == x3_values[z]:
            y3_values[z] += datatup[y][1]
plot(x3_values, y3_values, f"Total Yearly Rainfall (in Inches) from {year[0]} to {year[-1]}")