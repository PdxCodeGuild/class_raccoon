import string

alphabet = string.ascii_lowercase
num_chars = len(alphabet)
rot_amt = 13

string_input = input('Enter something to encrypt: ').lower()


string_output = ''
for i in string_input:
    char_loc = alphabet.index(i)
    new_loc = (char_loc + rot_amt) % num_chars
    string_output += alphabet[new_loc]

print(string_output)
