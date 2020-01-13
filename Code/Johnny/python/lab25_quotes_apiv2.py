# lab25_quotes_api.py
import requests
import json


page = 2
subject = input('Enter a keyword or subject: ').lower()
url = (f'https://favqs.com/api/quotes?page={page}&filter={subject}')
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers=headers)
data = json.loads(response.text)['quotes'] # turn the json into a python dictionary
# print(data) prints the dictionary with key

for body in data:
    body = body['body']
print('>>> '+body)
