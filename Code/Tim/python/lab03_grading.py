grade = int(input("What is the grade you\'d like to convert? "))
mod = ""
#grade modifier
if (grade % 10) >= 6:
    mod = "+"
elif (grade % 10) < 6 and (grade % 10) >= 4:
    mod = " "
elif (grade % 10) < 4:
    mod = "-"

#letter grade determination
if grade > 90:
    print("That grade is an A" + mod)
elif grade > 80:
    print("That grade is a B" + mod)
elif grade > 70:
    print("That grade is a C" + mod)
elif grade > 60:
    print("That grade is a D" + mod)
else:
    print("That grade is an F" + mod)
