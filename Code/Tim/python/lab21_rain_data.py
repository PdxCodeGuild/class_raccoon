import requests
import re
import datetime


# Function to pull all the URLs for the rain data
def get_rain_urls():
    rain_files = []
    response = requests.get('http://or.water.usgs.gov/non-usgs/bes/')
    page_source = response.text
    rain_files = re.findall(r'\w+\.rain', page_source)
    rain_files = ['https://or.water.usgs.gov/non-usgs/bes/' + rain_file for rain_file in rain_files]
    # print(rain_files)
    return rain_files

# Function to pull the text from one of the URLs
def pull_url_stuff(x):
    raw_text = requests.get(x[2])
    text = raw_text.text
    text.split('\n')
    return text

# Function to read URL text and create a data file
def get_data(rf):
    rainy_days = {}
    for i in rf:
        rainy_days = (re.findall(r'(\d{2}-\w+-\d{4})\s+(\d+)', rf))
    return rainy_days

get_rain_files = get_rain_urls()
text = pull_url_stuff(get_rain_files)
rainy_days = get_data(text)
print(text)
print(rainy_days)
