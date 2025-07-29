# pobranie pliku json o temperaturze itp i zapisnaie do zmiennej
import json 
import requests
weather_list = []
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=38.624&longitude=-90.195&current=temperature_2m,wind_speed_10m")
weather_list.append(response.json())

# zapisanie do pliku 

outfile = open('weather_list.json','w')
for report in weather_list:
  outfile.write(json.dumps(report)+"\n")
outfile.close()