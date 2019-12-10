# lab03_grading.py
"""
Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

Concepts Covered

input, print
type conversion (str to int)
comparisons (< <= > >=)
if, elif, else
Instructions

Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade
"""
# prompt student's input and convert to int
student = int(input("What's your grade? "))

# compare grade and print results
if student >= 90 and student <= 100:
    print("You got an A! ")
elif student >= 80 and student <= 89:
    print("You got a B. ")
elif student >= 70 and student <= 79:
    print("C student!")
elif student >= 60 and student <= 69:
    print("Grade D. ")
elif student >= 0 and student <= 59:
    print("Grade F. ")
else:
    print("Invalid number. ")
