#Provide a letter grade based on user number input
#actual input part
again = "Y"
while again == "Y":
    num_grade = input("What percentage did you get in the class? ")
    if num_grade.isdigit():
        num_grade = int(num_grade)
        #grading math
        if num_grade >= 90:
            print("You got an A")
        elif 80 <= num_grade <= 89:
            print("That's a B")
        elif 70 <= num_grade <= 79:
            print("Hey, C's get degrees m'dude")
        elif 60 <= num_grade <= 69:
            print("That's a D")
        elif num_grade <= 59:
            print("You failed bud")
        else:
            print("Please enter a valid grade")
    else:
        print("That's not even a number")
    again = input("Want to check another? (Y/N) ")
else:
    print("Bye")
