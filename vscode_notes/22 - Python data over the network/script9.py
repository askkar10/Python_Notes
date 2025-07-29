# improve formatting, called -> 'pretty printing' can make data structures much easier to understand
from pprint import pprint as pp
import json
import requests
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=41.882&longitude=-87.623&current=temperature_2m,wind_speed_10m")
# weather = json.loads(response.text) # zamiast tego mozemy tez użyć to:
weather = response.json()
pp(weather)