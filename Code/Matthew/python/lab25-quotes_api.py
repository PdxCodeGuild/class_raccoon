
import requests
import json



# while True:
#
#     quotes_url = 'https://api.chucknorris.io/jokes/random'
#     response = requests.get(quotes_url)
#     data = json.loads(response.text)
#     print(data['value'])
#
#     if input('would you like another quote? ') != 'yes':
#         break


response = requests.get('https://api.chucknorris.io/jokes/categories')
categories = json.loads(response.text)

while True:
    print('available categories:')
    print(', '.join(categories))

    category = input('enter a category to get a quote: ')
    if category == 'done':
        break

    response = requests.get('https://api.chucknorris.io/jokes/random?category=' + category)
    data = json.loads(response.text)
    print(data['value'])





# url = 'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
# response = requests.get(url)
# data = json.loads(response.text)
# print(data)






# url = 'https://favqs.com/api/quotes?page=1&filter=nature'
# headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
# response = requests.get(url, headers=headers)
# print(response.text)


# qotd_url = 'https://favqs.com/api/qotd'
# response = requests.get(qotd_url)
# data = json.loads(response.text)
# print(data['quote']['body'] + ' - ' + data['quote']['author'])







