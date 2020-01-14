'''
Lab: Sock Sorter
You've just finished laundry and your expansive sock collection is in complete disorder.
Sort your socks into pairs and pull out any loners.

Generate a list of 100 random socks, randomly chosen from a set of types: sock_types = ['ankle', 'crew', 'calf', 'thigh']

Find the number of duplicates and loners for each sock type. Hint: dictionaries are helpful here.

Version 2
Now you have a mix of types and colors. Represent socks using tuples containing one color and one type ('black', 'crew').
Randomly generate these, and then group them into pairs.

sock_colors = ['black', 'white', 'blue']
'''
import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']

# 1. choose 1,000 random types of sock, build a list of strings
# 2. start with an empty dictionary
# 3. loop over sock_types
# 4. if sock type in dictionary, += 1. else values = 1
# 5. mod each

random_socks = []

for i in range(1000):
    random_socks.append(random.choice(sock_types))

#print(random_socks)
sock_counts ={}
for sock in random_socks:
    sock_counts[sock] = sock_counts.get(sock, 0) + 1

print(sock_counts)

for key in sock_counts:
    pairs = sock_counts[key]//2
    loners = sock_counts[key]%2
