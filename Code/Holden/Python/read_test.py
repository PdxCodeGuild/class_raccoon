try:
    with open(r'RainData\dummy.rain', 'r') as file:
        content = file.read()
except FileNotFoundError:
    content = "no file found"

print(content)
