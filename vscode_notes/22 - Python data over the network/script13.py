# otwarcie weather_obj
import json
with open('weather_obj.json') as infile:
  weather_obj = json.load(infile)
print(weather_obj)