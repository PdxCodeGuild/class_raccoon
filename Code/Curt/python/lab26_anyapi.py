#lab26_anyapi.py

from secrets import mapapi #gets api key
import requests
import json
import geopy.distance #library to calculate distances between geocoords

print("Let's find out the distance between two US addresses!")

#Get address function
def getcoords():
    #get address from user
    add1 = input("Input the house number and street name (e.g. 1600 Wabash Ave): ")
    add2 = input("Input the city: ")
    add3 = input("Input the 2-letter state: ").upper()

    #join address components to use in map url string
    streetaddress = ', '.join((add1, add2, add3))
    streetaddress = streetaddress.replace(' ', '+')

    #access api using address string and api key
    map_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={streetaddress}&key={mapapi}'
    map_response = requests.get(map_url)
    #pull coordinates
    geocoords = json.loads(map_response.text)['results'][0]['geometry']['location']

    #return latitude and longitude as a tuple
    finalcoords = (geocoords['lat'],geocoords['lng'])
    print(type(finalcoords))
    return finalcoords

#call address function to create coordinates for both locations
print("First address:")
coords1 = getcoords()

print("Second address:")
coords2 = getcoords()

#get km or mi as unit of measurement
units = ''
while units != 'mi' and units != 'km':
    units = input("What units would you like to use: mi or km? ")

#return the distance in miles
if units == 'mi':
    distance = round(geopy.distance.geodesic(coords1, coords2).miles, 2)
    print(f'The distance between these two locations is {distance} miles.')

#return the distance in kilometers
if units == 'km':
    distance = round(geopy.distance.geodesic(coords1, coords2).km, 2)
    print(f'The distance between these two locations is {distance} kilometers.')
