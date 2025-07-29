# teraz otwarcie tego pliku 
import json
weather_list2 = []
for line in open('weather_list.json'):
  weather_list2.append(json.loads(line))
print(weather_list2)

outfile = open("weather_obj.json", "w")
weather_obj = {"reports": weather_list2, "count": 2}
json.dump(weather_obj, outfile)
outfile.close()