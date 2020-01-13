'''
Filename: lab25_api.py
Author: Dylan 
Purpose:
'''

import requests
import json
import helper

class QuotesApi:
    def __init__(self, url):
        self.keyword = ""
        self.page = 1
        self.turns = ['next','prev','keyword']
        self.url = url
    
    #json means javascript object notation
    def run_api(self):
        self.keyword = helper.text_checker(input("> "))
        if self.keyword == 'quit': #allows the user to quit 
            exit()
        url = self.url[0] + str(self.page) + self.url[1] + self.keyword
        print(url)
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        response = requests.get(url,headers=headers)
        data = json.loads(response.text) #turns into a python dictionary. load s is load into a string. load s => loads
        while True: #loops through each page and prints the results. Allows user to move on to next page. 
            print(f"Page: {self.page}\n")
            self.print_quotes(data)

            if data['last_page'] == True:
                print("This is the last page. Enter 'prev' for the previous page or hit ENTER to enter a new keyword. ")
                turn = helper.text_checker(input("> "))
                if turn == 'prev':
                    self.page -= 1
                else:
                    return 
            else:
                print("Enter 'prev' for the previous page, 'next' to continue to the next page, or 'keyword' to enter a new keyword..") #write exception for page1
                new_page = helper.text_checker(input("> "), self.turns)
                if new_page == 'keyword':
                    return
                elif new_page == 'prev':
                    if self.page == 1:
                        pass
                    else:
                         self.page -= 1
                else:
                    self.page += 1

    def print_quotes(self,data):
        i = 1   
        for quote in data["quotes"]:
            print(f"{i} - ", end=" ")
            if quote["id"] != 0:
                print(quote["body"])
            i += 1
        print()
        

if __name__ == "__main__":    
    cont = 'y'
    napi = QuotesApi(['https://favqs.com/api/quotes?page=','&filter='])
    while cont == 'y':
        print("enter a keyword to search for quotes, or enter 'quit' to exit the program. .")
        napi.run_api()



#print current page
#print quotes
#print next page is ____. Type next for next or prev for prev
#this is the last page. Type next to enter a new keyword