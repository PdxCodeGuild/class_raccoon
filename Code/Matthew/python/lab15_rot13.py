


import helpers




def encrypt(text, rot_amount):
    output = ''
    for char in text:
        # print(char, ord(char)-ord('a'))
        char_index = ord(char)
        if ord('a') <= char_index <= ord('z'):
            char_index -= ord('a')
            char_index += rot_amount
            char_index %= 26 # characters in the alphabet
            char_index += ord('a')
            char = chr(char_index)
            output += char
        elif ord('A') <= char_index <= ord('Z'):
            char_index -= ord('A')
            char_index += rot_amount
            char_index %= 26 # characters in the alphabet
            char_index += ord('A')
            char = chr(char_index)
            output += char
        else:
            output += char
    return output
        
        
        
        
        


if __name__ == '__main__':
    text = input('Please enter some text to encrypt: ')
    rot_amount = helpers.get_int('Please enter the rotation amount: ')
    output_text = encrypt(text, rot_amount)
    print(output_text)


    


