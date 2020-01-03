import requests
import re
import datetime
​
def get_rain_urls():
​
    response = requests.get('https://or.water.usgs.gov/non-usgs/bes/')
    page_source = response.text
    rain_files = re.findall(r'\w+\.rain', page_source)
    rain_files = ['https://or.water.usgs.gov/non-usgs/bes/' + rain_file for rain_file in rain_files]
    print(rain_files)
​
​
# recommended formats
​
data = [
    (datetime.datetime(2019, 10, 11), 12),
    (datetime.datetime(2019, 10, 12), 5),
]
​
data = [
    ((2019, 10, 11), 12),
    ((2019, 10, 12), 5)
]
