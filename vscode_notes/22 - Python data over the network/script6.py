# fetching data via an api
import requests
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=41.882&longitude=-87.623&current=temperature_2m,wind_speed_10m")
weather = response.text
print(weather)