import re

name_choice = input("Name: ").lower()
print(re.match('^[a-z]+$', name_choice))
