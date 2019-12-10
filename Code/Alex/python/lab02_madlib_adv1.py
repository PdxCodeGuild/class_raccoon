"Here is a list of the most (adjective) horror (plural noun) ever made in Hollywood! Each of these (adjective) films received a rating of two (part of the body(plural))-up from Siskel and Ebert. 1. The Hunch (part of the body) of Notre (noun). 2. The (noun) of the Living (noun). 3. (noun) of Frankenstein. 4. Invasion of the (noun) Snatchers. 5. (noun) from the (adjective) Lagoon. 6. Last (noun) on the Left. 7. The (noun) of the Opera"



#modules

import random

#variables and user inputs

x = list(input("Choose 3 adjectives: ").split())
print(x)
q = list(input("Choose 7 singular nouns: ").split())
print(q)
#is there a function i can use to capitalize them^?
c = input("Choose a plural noun: ")
d = input("Choose a part of the body: ")
e = input("Choose a part of the body (plural): ")


adj_list = random.choice(x)
noun_list = random.choice(q)


#mad lib calculation

print(f"\n\n\nHere is a list of the most {adj_list} horror {c} ever made in Hollywood!")
print(f"Each of these {adj_list} films received a rating of two {e}-up from Siskel and Ebert\n\n1. The Hunch {d} of Notre {noun_list}\n2. The {noun_list} of the Living {noun_list}\n3. {noun_list} of Frankenstein\n4. Invasion of the {noun_list} Snatchers\n5. {noun_list} from the {adj_list} Lagoon\n6. Last {noun_list} on the Left\n7. The {noun_list} of the Opera\n\n")
