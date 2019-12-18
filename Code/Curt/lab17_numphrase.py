#lab17_numphrase.py

print("Number to phrase!")

#Get the value
numval = -1
while numval <= 0 or numval >=1000:
    numval = input("Pick a number between 0-999: ")
    try:
        numval = int(numval)
        if numval <= 0 or numval >= 1000:
            print("Number outside of range!")
    except ValueError:
        print("Invalid entry!")

# determine digits
hundo_digit = numval//100
tens_digit = (numval-hundo_digit*100)//10
ones_digit = numval%10

# wordlists
oneslist = ["","one","two","three","four","five","six","seven","eight","nine"]
teenlist = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tenslist = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hundolist = []
for x in oneslist:
    hundo = x + " hundred "
    hundolist.append(hundo)

# create word
word = ""
if hundo_digit > 0:
    word += hundolist[hundo_digit]
if tens_digit > 1:
    word += tenslist[tens_digit]
    if ones_digit > 0:
        word += "-" + oneslist[ones_digit]
elif tens_digit == 1:
    word += teenlist[ones_digit]
elif ones_digit > 0:
    word = oneslist[ones_digit]
else:
    if hundo_digit == 0:
        word = "zero"

#print result
print(f"In English: {word}")

# VERSION 3 - Roman Numerals
roneslist = ["","I","V"]
rtenslist = ["","X","L"]
rhundolist = ["","C","D"]
rthouslist = ["","M"]

def roman_num(numlist, nextnumlist, digit):
    addword = word
    if digit == 9:
        addword += (numlist[1] + nextnumlist[1])
    elif digit < 9 and digit > 4:
        addword += numlist[2]
        for x in range(digit-5):
            addword += numlist[1]
    elif digit == 4:
        addword += (numlist[1]+numlist[2])
    elif digit < 4 and digit > 0:
        for x in range(digit):
            addword += numlist[1]
    else:
        addword += ""
    return addword

word=""
if hundo_digit > 0:
    word = roman_num(rhundolist, rthouslist, hundo_digit)
if tens_digit > 0:
    word = roman_num(rtenslist, rhundolist, tens_digit)
if ones_digit > 0:
    word = roman_num(roneslist, rtenslist, ones_digit)
if hundo_digit == 0 and tens_digit == 0 and ones_digit == 0:
    word = "There is no zero in Roman numerals!"

print(f"In Roman numerals: {word}")

# VERSION 4 - Check the time
check = False
while check is False:
    time = input("What is the time in digits (ex: 7:35)? ")
    time = time.split(":")
    flag = False
    for x in range(len(time)):
        try:
            time[x] = int(time[x])
        except ValueError:
            check = False
            flag = True
            print("Invalid entry!")
            break
    if flag:
        continue
    if time[0] > 0 and time[0] <= 12 and time[1] >= 0 and time[1] < 60 and len(time) == 2:
        hour = time[0]
        minute = time[1]
        check = True
    else:
        check = False
        print("Invalid time!")

def timecalc(numval):
    word = ""
    tens_digit = numval//10
    ones_digit = numval%10
    if tens_digit > 1:
        word += tenslist[tens_digit]
        if ones_digit > 0:
            word += "-" + oneslist[ones_digit]
    elif tens_digit == 1:
        word += teenlist[ones_digit]
    elif ones_digit > 0:
        word = oneslist[ones_digit]
    return word

timeword = ""
timeword += timecalc(hour) + " " + timecalc(minute)


print(f"The time is: {timeword}")
