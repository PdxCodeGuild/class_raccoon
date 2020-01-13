import requests
import json
def get_bad_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url) # send the request to the api
    # print(response.text) # look at the raw json
    data = json.loads(response.text) # turn the json into a python dictionary
    return(data['value']) # get a part of the response data out of the dictionary

# print(get_bad_joke())

def get_random_quote():
    url = "https://favqs.com/api/qotd"
    response = requests.get(url)
    # print(response.text)
    data = json.loads(response.text)["quote"]
    quote = data["body"]
    author = data["author"]

    return(f"\nYour quote of the day is: {quote} By {author}\n")
# print(get_random_quote())



keyword = input("Please choose a keyword: ")



page = 1
quote_count = 1
while True:
    
    url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
    headers = {'Authorization': 'Token token="ENTER TOKEN HERE"'} # I know you said that using your API key here wouldn't be a big deal, but I wanted to get into the habit of not uploading them to GIT
    
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)["quotes"]
    # print(data)
    if data[0]["body"] == "No quotes found":
        keyword = input("No quotes found. Please enter a new keyword: ")
        continue
    for key in data:
        print(f"Quote number {quote_count}")
        print(f"{key['body']}")
        print(f"Author: {key['author']}")
        quote_count += 1
        

        
            
    next_last_quit = input("Would you like to go to the next page, go back a page, or quit? ").lower()
    if "next" in next_last_quit:
        page += 1
    elif "back" in next_last_quit and page == 1:
        print("Page zero does not exist")
    elif "back" in next_last_quit:
        page -= 1
    elif "quit" in next_last_quit:
        print("Goodbye")
        break
    else:
        print("Invalid entry, please try again")