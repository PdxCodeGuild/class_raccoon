#lab03_grading.py

print("Let's find out what grade you got!")

gpa = int(round(float(input("Input your grade percentage (0-100): "))))
print(gpa)

if gpa >= 90:
    lt_grade = "A"
elif gpa >= 80:
    lt_grade = "B"
elif gpa >= 70:
    lt_grade = "C"
elif gpa >= 60:
    lt_grade = "D"
else:
    lt_grade = "F"

sp_grade = gpa%10

if gpa >= 100:
    symb = "+"
elif gpa < 60:
    symb = ""
elif sp_grade >= 8:
    symb = "+"
elif sp_grade <= 2:
    symb = "-"
else:
    symb = ""

print(f"Your final grade is {lt_grade}{symb}.")
