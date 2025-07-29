import json
with open('weather-01.json') as infile:
    weather_json = json.load(infile)

print(weather_json)