'''
Lab: Jackalope Simulator
Version 1
The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
With these conditions in mind, we can represent our population as a list of ints.
'''
 # 1. start with a list of jackalopes at age 0
 # 2. start year count at 0
 # 3. while len(listalopes) < 1000
 # 4. add 1 to each jackalopes range
 # 5. count how many are the breeding range , round down to the nearest even number
 # 6. add that number of new jackalopes
 # 7. kill the 10 year olds
 # 8. increment year

listalopes = [0, 0]
years = 0
while len(listalopes) < 1000:
    # print(years.len(listalopes))
    for i in range(len(listalopes)):
        listalopes[i] += 1

    num_in_age = 0
    for i in range(len(listalopes)):
        if 4 <= listalopes[i] < 9:
            num_in_age += 1
    num_in_age -= num_in_age%2
    # num_in_age = num_in_age//2*2

    for i in range(num_in_age):
        listalopes.append(0)

listalopes2 = []
for listalope in listalopes:
    if listalope < 10:
        listalopes2.append(listalope)
listalopes = listalopes2
years += 1

print(listalopes)
