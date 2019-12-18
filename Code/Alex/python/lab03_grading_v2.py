'''
Version 2 *not complete*

Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using if statements, or use modulus % to get the ones-digit to set another string to '+', '-', or ' '. Then you can concatenate that string with your grade string.
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
