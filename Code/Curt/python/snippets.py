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

dates = ['01-OCT-2019', '02-OCT-2019', '01-SEP-2019', '02-SEP-2019', '01-DEC-2019', '02-DEC-2019', '01-DEC-1980', '01-DEC-2021']
dates = [datetime.datetime.strptime(date, '%d-%b-%Y') for date in dates]
dates.sort(key=lambda x: x.month)
print('a', 'b', 'c', sep='-', end='!!!')
# dates.sort()
print(dates)

def add(a, b):
    return a + b
add = lambda a, b: a + b
add(5, 2)
