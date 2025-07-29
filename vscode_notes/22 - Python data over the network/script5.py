# retrieving files over http/https
# 'requests' -> the easiest and most reliable way to acces http/https servers
# pip install requests
# code patches the monthly temperature data for Heathrow airport sine 1948

import requests
response = requests.get("http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt")
print(response.text)