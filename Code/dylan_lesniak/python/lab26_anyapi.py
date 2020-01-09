#look at the documentation
#look at the endpoints
#find the url and if possible, enter into the browser

from secrets import api_key

import requests
import json
import helper
import string


#because of issues with requests per second, I can't get the worldwide information. So instead I'm doing for just USA
#later versions can potentially choose country, but for now, I'll just allow to choose state. 
class AirApi:
    def __init__(self):
        self.key = api_key
        self.info_urls = { #all following urls must be preceded by http:// and succeeded by the api_key
            #The key indicates what values will be returned. If you want a list of the countries, use the 'countries' key. 
            'countries':['api.airvisual.com/v2/countries?key='],
            'states':['api.airvisual.com/v2/states?country=','&key='],
            'cities': ['api.airvisual.com/v2/cities?state=','&country=','&key='],
            'city':['api.airvisual.com/v2/city?city=','&state=','&country=','&key=']
        }
        self.countries_data = {} #will hold all the data the other variables will be drawn from in a hash form 
        self.countries = []
        self.country = ""
        self.states = []
        self.state = ""
        self.cities = []
        self.city = ""
        self.city_data = {}
        self.ok_formats = string.ascii_letters + string.punctuation
        

    def get_data(self):
        response = requests.get("http://" + self.info_urls['countries'][0] + self.key) #don't think I need any header...
        self.countries_data = json.loads(response.text) 
        for keys in self.countries_data['data']:
            self.countries.append(keys['country'])

    def populate_states(self):
        print(f"\nAvailable countries are: ",end= ' ')
        i = 0 
        for country in self.countries:
            if i == len(self.countries) - 1:
                print(country)
            else:
                print(country + ",",end=' ')
            i += 1
        print("\nWhich country would you like information from? ")
        self.country = helper.text_checker(input("> "), self.countries, self.ok_formats)
        response = requests.get('http://' + self.info_urls['states'][0] + self.country + self.info_urls['states'][1] + self.key)
        states_dict = json.loads(response.text)['data'] #this gives us a list of dictionaries, where each dictionary is a state
        for state in states_dict:
            self.states.append(state['state'])
        
    def populate_cities(self):
        print(f"\nAvailable states are: ",end= ' ')
        i = 0 
        for state in self.states:
            if i == len(self.states) - 1:
                print(state)
            else:
                print(state + ",",end=' ')
            i += 1
        print("\nWhich state would you like information from? ")
        self.state = helper.text_checker(input("> "), self.states, self.ok_formats)
        response = requests.get('http://' + self.info_urls['cities'][0] + self.state + self.info_urls['cities'][1] + self.country + self.info_urls['cities'][2] + self.key)
        cities_dict = json.loads(response.text)['data'] #this gives us a list of dictionaries, where each dictionary is a city
        for city in cities_dict:
            self.cities.append(city['city'])

    def get_city_data(self):
        print(f"\nAvailable cities are: ",end= ' ')
        i = 0 
        for city in self.cities:
            if i == len(self.cities) - 1:
                print(city)
            else:
                print(city + ",",end=' ')
            i += 1
        print("\nWhich city would you like information from? ")
        self.city = helper.text_checker(input("> "), self.cities, self.ok_formats)
        response = requests.get('http://' + self.info_urls['city'][0] + self.city + self.info_urls['city'][1] + self.state + self.info_urls['city'][2] + self.country + self.info_urls['city'][3] + self.key)
        self.city_data = json.loads(response.text)
        
    
    def print_city_data(self):
        aqi = self.city_data['data']['current']['pollution']['aqius']
        print(f"The AQI of {self.city} is {aqi}.")
        if aqi > 300:
            print("The Air Quality is EXTREMELY HAZARDOUS. Just don't go here.")
        elif aqi > 200:
            print("The Air Quality here is Very Unhealthy. Everyone may experience more serious health effects.")
        elif aqi > 150:
            print("The Air Quality here is Unhealthy. Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.")
        elif aqi > 100:
            print("The Air Quality here is Unhealthy for Sensitive Groups. Members of sensitive groups may experience health effects. The general public is not likely to be affected.")
        elif aqi > 50: 
            print("The Air Quality here is Moderate. Members of sensitive groups may experience health effects. The general public is not likely to be affected.")
        else:
            print("The Air Quality here is Good. Air quality is considered satisfactory, and air pollution poses little or no risk.")



    def run_api(self):
        self.get_data()
        self.populate_states()
        self.populate_cities()
        self.get_city_data()
        self.print_city_data()
            

if __name__ == "__main__":
    cont = 'y'
    while cont == 'y':
        new_api = AirApi()
        new_api.run_api()
        print("Would you like to choose another city? (y/n)")
        cont = helper.text_checker(input("> "), ['y','n'])
