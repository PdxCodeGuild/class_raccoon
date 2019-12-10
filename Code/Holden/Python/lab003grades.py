input("welcome to the grade converter.")
usr=float(input("Please enter your grade percentage: "))
usrl=usr//10
usrm=usr%10
#print(usrl)
if usrl > 10:
    ltr="Neeerd"
elif usrl > 9:
    if usrm > 0:
        ltr="Did you even need to do that extra credit? A++"
    else:
        ltr="A+"
elif usrl > 8:
    ltr="you got an A"
elif usrl > 7:
    ltr="you got a B"
elif usrl > 6:
    ltr="you got a C"
elif usrl > 5:
    ltr="you got a D"
else:
    ltr="you got an F"
if 5 < usrl < 10:
    if usrm >= 7:
        ltr=ltr+"+"
    elif usrm < 3:
        ltr=ltr+"-"
print(ltr)
