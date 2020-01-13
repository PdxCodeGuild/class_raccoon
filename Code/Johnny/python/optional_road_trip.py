# optional_road_trip.py

# Traveling from one city to an adjacent one is called a hop. Let the user enter a city. Print out all the cities connected to that city. Then print out all cities that could be reached through two hops.


city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

# join dictionary without ','
# s = " "
# s = s.join(city_to_accessible_cities)

print('Pick a city for your one hop road trip.')
for key in city_to_accessible_cities:
    print(key)

user_city = input('>>> ').lower()
if user_city == 'boston':
    print(city_to_accessible_cities['Boston'])
elif user_city == 'new york':
    print(city_to_accessible_cities['New York'])
elif user_city == 'albany':
    print(city_to_accessible_cities['Albany'])
elif user_city == 'portland':
    print(city_to_accessible_cities['Portland'])
elif user_city == 'philadelphia':
    print(city_to_accessible_cities['Philadelphia'])
else:
    print('Invalid city.')
