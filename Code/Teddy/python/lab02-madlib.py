animal = input("What is your favorite animal?:...")
veggi = input("Vegetable:...")
hungry = input("The felling when you want to eat:...")
size = input("Your shirt size:...")

print("Let's play a madlibs game")
print(f'''
\nToday I went to the zoo.
\nI saw a {animal} jumping up and down in its tree.
\nI got some {veggi} and passed them through the cage above my head.
\nFeeding that animal made me {hungry}.
\nI went to get a {size} scoop of ice cream.\n''')

play_again = input("Do you want to play again? (y/n)").lower()



while play_again == "y":

    animal = input("What is your favorite animal?:...")
    veggi = input("Vegetable:...")
    hungry = input("The felling when you want to eat:...")
    size = input("Your shirt size:...")

    print("Let's play a madlibs game")
    print(f'''
    \nToday I went to the zoo.
    \nI saw a {animal} jumping up and down in its tree.
    \nI got some {veggi} and passed them through the cage above my head.
    \nFeeding that animal made me {hungry}.
    \nI went to get a {size} scoop of ice cream.\n''')

    play_again = input("Do you want to play again? (y/n)").lower()
else:
    print("bye")
