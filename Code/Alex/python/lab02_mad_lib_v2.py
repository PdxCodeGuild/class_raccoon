'''
Version 2 (optional)

Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.
Add randomness! Use the random module, rather than selecting which adjective goes where in the story.
'''

#modules

import random

#variables and user inputs
adj_list = list(input("Choose 3 adjectives: ").split(" "))#made a list of the inputs so that i can call on it later
for i in range(len(adj_list)):#i wanted to capitalize the words so they would be in context with the mad lib i chose
    adj_list[i] = adj_list[i].capitalize()

#same thing
singular_noun_list = list(input("Choose 7 singular nouns: ").split(" "))
for i in range(len(singular_noun_list)):
    singular_noun_list[i] = singular_noun_list[i].capitalize()

#easy. no lists
plural_noun = input("Choose a plural noun: ")

body_part = input("Choose a part of the body: ").capitalize()

body_part_plural = input("Choose a part of the body (plural): ")

#split(' ') = split wherever there's a space

#mad lib calculation

print(f"\n\n\nHere is a list of the most {random.choice(adj_list).lower()} horror {plural_noun} ever made in Hollywood!")
print(f"Each of these {random.choice(adj_list).lower()} films received a rating of two {body_part_plural}-up from Siskel & Ebert\n\n1. The Hunch {body_part} of Notre {random.choice(singular_noun_list)}\n2. The {random.choice(singular_noun_list)} of the Living {random.choice(singular_noun_list)}\n3. {random.choice(singular_noun_list)} of Frankenstein\n4. Invasion of the {random.choice(singular_noun_list)} Snatchers\n5. {random.choice(singular_noun_list)} from the {random.choice(adj_list)} Lagoon\n6. Last {random.choice(singular_noun_list)} on the Left\n7. The {random.choice(singular_noun_list)} of the Opera\n\n")
