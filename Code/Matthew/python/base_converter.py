



def convert_base(x, base):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = ''
    while x > 0:
        output = alphabet[x%base] + output
        x //= base
    return output


print(convert_base(5, 16))
print(convert_base(128, 16))

