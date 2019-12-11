

import random
import string




def random_password1(n):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(n):
        password += random.choice(alphabet)
    return password



# n = input('How many characters should the password be? ')
# print(random_password(n))


def random_password2(n_lower, n_upper, n_digits, n_punctuation):
    password = ''
    for i in range(n_lower):
        password += random.choice(string.ascii_lowercase)
    for i in range(n_upper):
        password += random.choice(string.ascii_uppercase)
    for i in range(n_digits):
        password += random.choice(string.digits)
    for i in range(n_punctuation):
        password += random.choice(string.punctuation)
    
    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    
    return password

def get_int(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print('please enter a valid integer')

n_lower = get_int('How many lowercase letters? ')
n_upper = get_int('How many uppercase letters? ')
n_digits = get_int('How many digits? ')
n_punctuation = get_int('How many punctuation characters? ')
print(random_password2(n_lower, n_upper, n_digits, n_punctuation))


