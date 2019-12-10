'''
Filename: Grading
Author: Dylan
Purpose: Take user number input and convert to a letter grade, complete with +/-
'''

def grading():
    print("Welcome! Please insert your number grade (0-100). ")
    user_grade = input("> ")
    while not user_grade.isdigit():
        print("Invalid entry. Please enter a number. (0-100)")
        user_grade = input("> ")
    user_grade = int(user_grade)
    while user_grade > 100: 
        print("You're not that smart. Please keep responses between (0-100). ")
        user_grade = input("> ")
        while not user_grade.isdigit():
            print("Invalid entry. Please enter a number. (0-100)")
            user_grade = input("> ")
        user_grade = int(user_grade)
    letter_grade = letter(user_grade)
    letter_grade += plus_minus(user_grade)
    print(f"Your grade is a(n) {letter_grade}. ")
    
def letter(user_grade):
    #take grade and turn to letter
    letter = ""
    if user_grade < 60:
        letter = "F"
    elif user_grade < 70:
        letter = "D"
    elif user_grade < 80:
        letter = "C"
    elif user_grade < 90: 
        letter = "B"
    else:
        letter = "A"
    return letter

def plus_minus(user_grade):
    #use % to create distinctions. 
    #but make 100 an A+ and anything below 60 an F. 
    add_on = ""
    if user_grade == 100:
        add_on = "+"
    elif user_grade < 60:
        add_on = ""
    elif user_grade % 10 > 6:
        add_on = "+"
    elif user_grade % 10 < 4:
        add_on = "-"
    else:
        add_on = ""
    return add_on

cont = "y"
while cont == "y":
    grading()
    print("Would you like to enter a new grade? (y/n)")
    cont = input("> ").lower()

exit()