import string

alphabet = string.ascii_lowercase
num_chars = len(alphabet)


string_input = input('Enter something to encrypt: ').lower()
user_rot = int(input('Enter a encryption number: '))

rot_amt = user_rot
string_output = ''
for i in string_input:
    char_loc = alphabet.index(i)
    new_loc = (char_loc + rot_amt) % num_chars
    string_output += alphabet[new_loc]

print(string_output)
