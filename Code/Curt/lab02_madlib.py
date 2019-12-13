#lab02_madlib.py
print("Welcome to Madlibs!\n")
import string
import random

# Advanced Version 3 - Multiple entries

auth_name = input("What is your name? ")
adj1 = input("Give me an adjective: ")
pres_par = input("Now give me a present participle (a verb ending in -ing): ")
time1 = input("Give me a past-tense temporal noun (yesterday, last week, etc): ")
time2 = input("Give me a unit of time (second, year, etc): ")

#relatives list
rel_lst = ""
while len(rel_lst) != 2:
    rel = input("Name two types of relatives (father, brother, meemaw), separated by commas: ").replace(", ",",")
    rel_lst = rel.split(",") #turn into list
    rel_lst = [x.lower() for x in rel_lst] #Lower and replace

#plural nouns list
plnoun_lst = ""
while len(plnoun_lst) != 2:
    plnoun1 = input("Give two plural nouns, separated by commas: ").replace(", ",",")
    plnoun_lst = plnoun1.split(",") #turn into list
    plnoun_lst = [x.lower() for x in plnoun_lst] #Lower and replace

#past-tense verb list
past_vb_lst = ""
while len(past_vb_lst) != 3:
    past_vb1 = input("Give three past-tense verbs, separated by commas: ").replace(", ",",")
    past_vb_lst = past_vb1.split(",") #turn into list
    past_vb_lst = [x.lower() for x in past_vb_lst] #Lower and replace

#nouns list
noun_lst = ""
while len(noun_lst) != 5:
    noun1 = input("Give me five nouns, separated by commas: ").replace(", ",",")
    noun_lst = noun1.split(",") #turn into list

#verbs list
verb_lst = ""
while len(verb_lst) != 7:
    verb1 = input("Last one! Give seven verbs (present tense),\nseparated by commas: ").replace(", ",",")
    verb_lst = verb1.split(",") #turn into list
    verb_lst = [x.lower() for x in verb_lst] #Lower and replace

input("Here's the original poem:\n")
print("THE LOSER")
print("by Shel Silverstein\n")
print("Mama said I'd lose my head")
print("If it wasn't fastened on.")
print("Today I guess it wasn't")
print("'Cause while playing with my cousin")
print("It fell off and rolled away")
print("And now it's gone.")
input("[CONT]")
print("And I can't look for it")
print("'Cause my eyes are in it,")
print("And I can't call to it")
print("'Cause my mouth is on it")
print("(Couldn't hear me anyway")
print("'Cause my ears are on it),")
print("Can't even think about it")
print("'Cause my brain is in it.")
print("So I guess I'll sit down")
print("On this rock")
print("And rest for just a minute...")
input("")

input("And now here's your poem:")
print(f"THE {noun_lst[0]}".upper())
print(f"by {auth_name}\n")
print(f"{rel_lst[0].capitalize()} said I'd {verb_lst[0]} my {noun_lst[1]}")
print(f"If it wasn't {past_vb_lst[0]} on.")
print(f"{time1.capitalize()} I guess it wasn't")
print(f"'Cause while {pres_par} with my {rel_lst[1]}")
print(f"It {past_vb_lst[1]} off and {past_vb_lst[2]} away")
print(f"And now it's {adj1}.")
input("[CONT]")
print(f"And I can't {verb_lst[1]} it")
print(f"'Cause my {plnoun_lst[0]} are in it,")
print(f"And I can't {verb_lst[2]} it")
print(f"'Cause my {noun_lst[2]} is on it")
print(f"(Couldn't {verb_lst[3]} me anyway")
print(f"'Cause my {plnoun_lst[1]} are on it),")
print(f"Can't even {verb_lst[4]} it")
print(f"'Cause my {noun_lst[3]} is in it.")
print(f"So I guess I'll {verb_lst[5]} down")
print(f"On this {noun_lst[4]}")
print(f"And {verb_lst[6]} for just a(n) {time2}...")
