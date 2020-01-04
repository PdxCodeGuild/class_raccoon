#rot 13 lab
import string

alphabet = string.ascii_letters + string.punctuation + string.digits

def encrypt(user_pass,num_times):
    encrypted = ""
    for x in (user_pass):
        i = alphabet.find(x) + num_times
        encrypted += alphabet[i % len(alphabet)]
    return encrypted

        
#Program exectuion for taking a users password that includes uppercase, lowercase, numbers and special characters and allows them to select how many rotations they want to do. 

user_pass = input("Enter a password using letters from the alphabet. ie. 'Bhnk6%kn'\n:")
how_many = input("How many times do you want to iterate over the chars?:\n")
how_many = int(how_many)
print(encrypt(user_pass,how_many))
