'''
Version 3 (optional)

Make it a repeatable game. Once you're done prompting the user for words, prompt them for whether they'd like to hear the story. Use a while loop to keep asking if they'd like to hear the story again until the answer is 'no'. You could then ask them if they'd like to make another story, and so on.
Key Concepts

Variables
String formatting
Handling user input
'''

#modules
import random

print(f"\n\nLet's play a madlib horror game!\n\n")

#making game repeatable
play_again = "yes"

while play_again == "yes":

    #variables and user inputs
    adj_list = list(input("\n\n\n\nChoose 3 adjectives: ").split(" "))

    if range(len(adj_list)) != 2:
        print("\nincorrect amount of adjectives used")

    for i in range(len(adj_list)):
        adj_list[i] = adj_list[i].capitalize()

    singular_noun_list = list(input("Choose 7 singular nouns: ").split(" "))
    for i in range(len(singular_noun_list)):
        singular_noun_list[i] = singular_noun_list[i].capitalize()

    plural_noun = input("Choose a plural noun: ")
    body_part = input("Choose a part of the body: ").capitalize()
    body_part_plural = input("Choose a part of the body (plural): ")


    #mad lib calculation

    print(f"\n\n\nHere is a list of the most {random.choice(adj_list).lower()} horror {plural_noun} ever made in Hollywood!")
    print(f"Each of these {random.choice(adj_list).lower()} films received a rating of two {body_part_plural}-up from Siskel & Ebert\n\n1. The Hunch {body_part} of Notre {random.choice(singular_noun_list)}\n2. The {random.choice(singular_noun_list)} of the Living {random.choice(singular_noun_list)}\n3. {random.choice(singular_noun_list)} of Frankenstein\n4. Invasion of the {random.choice(singular_noun_list)} Snatchers\n5. {random.choice(singular_noun_list)} from the {random.choice(adj_list)} Lagoon\n6. Last {random.choice(singular_noun_list)} on the Left\n7. The {random.choice(singular_noun_list)} of the Opera\n\n")

    play_again = input("Would you like to play again?\n").lower()

    while play_again != "no" and play_again != "yes":
        print(f"\ninvalid input.")
        play_again = input("\nWould you like to play again?\n").lower()

    if play_again == "no":
        print("\nokay bye\n╭∩╮ಠ_ಠ_/¯\n")
        break

'''Here is a list of the most (adjective) horror (plural noun) ever made in Hollywood! Each of these (adjective) films received a rating of two (part of the body(plural))-up from Siskel and Ebert. 1. The Hunch (part of the body) of Notre (noun). 2. The (noun) of the Living (noun). 3. (noun) of Frankenstein. 4. Invasion of the (noun) Snatchers. 5. (noun) from the (adjective) Lagoon. 6. Last (noun) on the Left. 7. The (noun) of the Opera'''
