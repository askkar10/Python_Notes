from pprint import pprint as pp
import requests
import json
response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=41.882&' \
'longitude=-87.623&current=temperature_2m,wind_speed_10m')
weather = response.json()
outfile = open('weather-01.json','w')
json.dump(weather,outfile)
outfile.close()
json.dumps(weather,indent=2)
