# Lab 03 Grading

user_input = float(input('What is your score (0 - 100)?'))

# 90-100: A
if user_input in range(90, 101):
    print('Your grade is A')

# 80-89: B
elif user_input in range (80, 90):
    print('Your grade is B')

# 70-79: C
elif user_input in range (70, 80):
    print('Your grade is C')

# 60-69: D
elif user_input in range (60, 70):
    print('Your grade is D')

# 0-59: F
elif user_input in range (0, 60):
    print('Your grade is F')

else:
    print('Score have to be 0-100')
