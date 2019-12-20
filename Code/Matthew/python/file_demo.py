

file_path = 'test.txt' # relative
file_path = r'..\..\..\1 Python\data\apothecary.txt' # relative
file_path = r'C:\Users\flux\programs\class_raccoon\1 Python\data\apothecary.txt' # absolute

with open(file_path, encoding='utf-8') as f:
    contents = f.read()

lines = contents.split('\n')
lines = [line.upper() for line in lines]
lines = [line for line in lines if line != '']
print(lines)
# processing


