#lab03 Grading Lab, Brandon G.


#Grading Function

def grading(a):
    if a in range(90,100):
        if a > 97:
            print("A+")
        elif a >= 93 < 97:
            print("A")
        else:
            print("A-")
    elif a in range(80,89):
        if a > 87:
            print("B+")
        elif a >= 83 < 87:
            print("B")
        else:
            print("B-")
    elif a in range(70,79):
        if a > 77:
            print("C+")
        elif a >= 73 < 77:
            print("C")
        else:
            print("C-")
    elif a in range(60,69):
        if a > 67:
            print("D+")
        elif a >= 63 < 67:
            print("D")
        else:
            print("D-")
    elif a in range(0,59):
        print("You Suck")



#Program run

print("Welcome to the grading app. \n")
# user_grade = input("What was your test score?: ")
# user_grade = int(user_grade)
# grading(user_grade)

user_input = "yes"
while user_input == "yes":
    user_grade2 = input("What was your test score?: ")
    user_grade2 = int(user_grade2)
    grading(user_grade2)
    user_input = input("Again?: ").lower()
else:
    print("goodbye")
