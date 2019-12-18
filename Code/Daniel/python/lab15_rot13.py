#rot13 encryption
import string
user_phrase = input("What would you like to encrypt: ").lower()
user_encrypt = int(input("What would you like to encrypt it by: "))

alphabet = string.ascii_lowercase + string.digits + string.punctuation + " "
#encrypts user input by adding a user defined number to the index of every letter
def encrypt(user_phrase, user_encrypt):
    encrypted_phrase = ""
    for i in range(len(user_phrase)):
        x = alphabet.find(user_phrase[i]) + user_encrypt
        encrypted_digit = alphabet[x%(len(alphabet))]
        encrypted_phrase += encrypted_digit
    return encrypted_phrase
mid_encrypt = encrypt(user_phrase, user_encrypt)
#same as above, but it subtracts the chosen number from the index of the now encrypted word
def decrypt(mid_encrypt, user_encrypt):
    decrypted_phrase = ""
    for i in range(len(mid_encrypt)):
        x = alphabet.find(mid_encrypt[i]) - user_encrypt
        decrypted_digit = alphabet[x%(len(alphabet))]
        decrypted_phrase += decrypted_digit
    return decrypted_phrase
decrypted_phrase = decrypt(mid_encrypt, user_encrypt)
print(f"Your encrypted phrase is {mid_encrypt}, which is {decrypted_phrase}")



