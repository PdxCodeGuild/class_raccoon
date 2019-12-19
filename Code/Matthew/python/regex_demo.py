


import requests
import re


age = input('what is your age?')
if re.match('\d+', age):
    print('valid')
else:
    print('invalid')

quit()


response = requests.get('http://google.com/', headers={'User-Agent': 'Mozilla/5.0'})
text = response.text

# raw strings ignore escape sequences
# print('hello\n\tworld!\\')
# print(r'hello\n\tworld!\\')

colors = re.findall(r'#[0-9a-f]{3,6}', text)
print(colors)

