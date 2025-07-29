# improve formatting, called -> 'pretty printing' can make data structures much easier to understand
from pprint import pprint as pp
import json
import requests
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=41.882&longitude=-87.623&current=temperature_2m,wind_speed_10m")
# weather = json.loads(response.text) # zamiast tego mozemy tez użyć to:
weather = response.json()

# if you want to write your weather report to a json file u must do the following
outfile = open('weather-02.json','w')
json.dump(weather, outfile)
outfile.close()
# json.dumps(weather)

# zeby nie zapisywac pliku json w jednej linii
json.dumps(weather, indent=2)