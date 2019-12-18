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

grade = int(input("\n\n\n\nHello, welcome to the grade conversion.\n\nWhat is your score?  "))

if 90 < grade <= 100:
    print(f"\nA {grade} is a A\n\n\n\n")
elif 80 < grade < 89:
    print(f"\nA {grade} is a B\n\n\n\n")
elif 70 < grade < 79:
    print(f"\nA {grade} is a C\n\n\n\n")
elif 60 < grade < 69:
    print(f"\nA {grade} is a D\n\n\n\n")
elif 0 <= grade < 59:
    print(f"\nA {grade} is an F\n\n\n\n")
else:
    print("\ninvalid entry\n")
