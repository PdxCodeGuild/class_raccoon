import string
base_letters = string.ascii_lowercase

def encode(usin, rot):
    output = []
    for l in usin:
        if l in base_letters:
            leti = base_letters.find(l) + int(rot)
            output.append(base_letters[leti%len(base_letters)])
        else:
            output.append(l)
    stringout = "".join(output)
    return stringout

def decode(usin, rot):
    output = []
    for l in usin:
        if l in base_letters:
            leti = base_letters.find(l) - int(rot)
            output.append(base_letters[leti%len(base_letters)])
        else:
            output.append(l)
    stringout = "".join(output)
    return stringout

def exec(usin, encdec, rot):
    if encdec == 'encode':
        return encode(usin, rot)
    elif encdec == 'decode':
        return decode(usin, rot)
    else:
        return None
