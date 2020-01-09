


import json
import requests

while True:
    command = input('enter a command: ')
    if command == 'quit':
        break
    elif command == 'random':
        url = 'https://quote-garden.herokuapp.com/quotes/random'
        response = requests.get(url)
        print(response.text)
        # data = json.loads(response.text)
        data = response.json()
        print(data['quoteText'] + ' - ' + data['quoteAuthor'])
    elif command == 'keyword':
        # prompt for keyword
        keyword = input('enter a keyword: ')
        url = 'https://quote-garden.herokuapp.com/quotes/search/' + keyword
        response = requests.get(url)
        data = response.json()

        quotes = [(quote['quoteText'], quote['quoteAuthor']) for quote in data['results']]
        quotes = list(set(quotes))
        print(f'{len(quotes)} quotes found:')
        for quote in quotes:
            print(quote[0] + ' - ' + quote[1])
            print()
        # for quote in data['results']:
        #     print(quote['quoteText'] + ' - ' + quote['quoteAuthor'])
        #     print()
    else:
        print('command not recognized')


