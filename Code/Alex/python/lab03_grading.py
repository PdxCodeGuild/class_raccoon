'''
Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade
Numeric Ranges

90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
'''

print("Hello, welcome to the grade conversion.")
grade = input("What is your score: ")
grade = int(grade)
if 90 < grade <= 100:
    print("A")
elif 80 < grade < 89:
    print("B")
elif 70 < grade < 79:
    print("C")
elif 60 < grade < 69:
    print("D")
elif 0 <= grade < 59:
    print("F")
else:
    print("invalid entry")
