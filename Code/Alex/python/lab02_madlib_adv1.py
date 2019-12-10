"Here is a list of the most (adjective) horror (plural noun) ever made in Hollywood! Each of these (adjective) films received a rating of two (part of the body(plural))-up from Siskel and Ebert. 1. The Hunch (part of the body) of Notre (noun). 2. The (noun) of the Living (noun). 3. (noun) of Frankenstein. 4. Invasion of the (noun) Snatchers. 5. (noun) from the (adjective) Lagoon. 6. Last (noun) on the Left. 7. The (noun) of the Opera"



#modules

import random

#variables and user inputs

adj_list = list(input("Choose 3 adjectives: ").split(" "))
for x in range(len(adj_list)):
    adj_list[x] = adj_list[x].capitalize()

singular_noun_list = list(input("Choose 7 singular nouns: ").split(" "))
for x in range(len(singular_noun_list)):
    singular_noun_list[x] = singular_noun_list[x].capitalize()

plural_noun = input("Choose a plural noun: ")

pob = input("Choose a part of the body: ")
for x in range(len(pob)):
    pob[x] = pob[x].capitalize()
    
pob_plural = input("Choose a part of the body (plural): ")



#to do for next advanced version
'''#plural nouns list
plnoun_lst = ""
while len(plnoun_lst) != 2:
    plnoun1 = input("Give two plural nouns, separated by commas: ").replace(", ",",")
    plnoun_lst = plnoun1.split(",") #turn into list
    plnoun_lst = [x.lower() for x in plnoun_lst] #Lower and replace
'''


#mad lib calculation

print(f"\n\n\nHere is a list of the most {random.choice(adj_list)} horror {plural_noun} ever made in Hollywood!")
print(f"Each of these {random.choice(adj_list)} films received a rating of two {pob_plural}-up from Siskel & Ebert\n\n1. The Hunch {pob} of Notre {random.choice(singular_noun_list)}\n2. The {random.choice(singular_noun_list)} of the Living {random.choice(singular_noun_list)}\n3. {random.choice(singular_noun_list)} of Frankenstein\n4. Invasion of the {random.choice(singular_noun_list)} Snatchers\n5. {random.choice(singular_noun_list)} from the {random.choice(adj_list)} Lagoon\n6. Last {random.choice(singular_noun_list)} on the Left\n7. The {random.choice(singular_noun_list)} of the Opera\n\n")
