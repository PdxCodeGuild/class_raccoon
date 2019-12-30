#snippets.py

# allchar = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
# string.whitespace
# text = [c for c in text if c not in string.punctation + string.whitespace]
#
# def seedgen(phrase, elem):
#     cipher = list(elem)
#     seedval = input(phrase)
#     random.seed(seedval)
#     random.shuffle(cipher)
#     cipher = ''.join(cipher)
#     return cipher

# def inputcheck():
#     while isinstance(num2, float) == False:
#         num2 = input("What is the second number? ")
#         try:
#             num2 = float(num2)
#         except ValueError:
#             print("Invalid entry!")

file_path = r'..\..\1 Python\data\apothecary.txt'
with open('test.txt') as f:
    contents = f.read()

lines = contents.split()
lines = [line.upper() for line in lines]
lines = [line for line in lines if line != '']
print(lines)
#processing
