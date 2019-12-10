#madlibs lab

print ("\nWelcome to Madlibs!")

first_name = input("What is your name?")

print(f"Hey {first_name}! Thank you for playing")

def madlibs():
    noun = input("\nChoose a city\n")
    country = input("\nPick a country\n")
    name = input("\nPick a name of a place, any name\n")
    language = input("\nWhat is your favorite language?\n")
    animal = input("\nWhat is your favorite animal\n")
    body_part = input("\nPick a name of a body part\n")


    return (f"Thanks! Here is your madlib! \n{noun} was originally discovered by {country} in 1904, they named it {name}, which of course in {language} means a {animal} {body_part}. We better just call it {noun}. ")

print(madlibs())

playagain = input("Do you want to play again? yes or no.\n")
while playagain == "yes":
    print(madlibs())
else:
    print("goodbye!")
