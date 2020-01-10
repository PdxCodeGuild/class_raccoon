# lab26_any_api.py
# https://uinames.com/api/
# random people/name api
import string
import requests
import json
import webbrowser



print('Generate testimonial to add to your business.')
print('Pick random or enter attribute and create your own.')
print('-'*45)
print('Random           Random profile.')
print('Region           Add a country.')
print('Email            Attach a email to the profile.')
print('Phone            Add a phone number.')
print('Photo            Inlude a photo.')
print('Testimonial      Random testimonial.') # Testimonial is from Kayne West quotes
print('Create           Create profile.')
print('Quit')
print('-'*45)

url = 'https://uinames.com/api/'
PARAMS = 'ext'
response = requests.get(url, PARAMS)
data = json.loads(response.text)

quotes = 'https://api.kanye.rest'
response2 = requests.get(quotes)
data2 = json.loads(response2.text)

profile_dict = {'name': data['name'],
                'gender': data['gender'],
                'region': data['region'],
                'phone': data['phone'],
                'email': data['email'],
                'testimonial': data2['quote'],
                'photo': data['photo']}

profile = []
while True:
    user_input = input('>> ').lower()
    if user_input == 'random':
        print(f"Picture: {data['photo']}")
        print(f"Name:    {data['name']}")
        print(f"Gender:  {data['gender']}")
        print(f"Region:  {data['region']}")
        print(f"Phone:   {data['phone']}")
        print(f"Email:   {data['email']}")
        print(f"Testimonial: ")
        print(" >>> " + data2['quote'])
        break
    elif user_input == 'create' or user_input == 'quit':
        break
    results = profile_dict.get(user_input)
    profile.append(results)
print('\n'.join(profile))
webbrowser.open(data['photo'], new=2)
