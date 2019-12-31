import re
with open(r'FFPy\crime_data.csv', 'r') as file:
    clean = file.read()
    clean = re.sub(r" +,",",",clean)
with open(r'FFPy\crime_data.csv', 'w') as file:
    file.write(clean)
