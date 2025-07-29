import requests
response = requests.get('http://www.metoffice.gov.uk/pub/data/' \
'weather/uk/climate/stationdata/heathrowdata.txt')
print(response.text)