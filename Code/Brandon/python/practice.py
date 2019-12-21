import requests

respsonse = requests.get('https://google.com')

print(respsonse.text)