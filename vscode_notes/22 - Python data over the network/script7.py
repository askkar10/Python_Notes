# crime data for chicago betwwen noon and 1 p.m
# on january 10, 2017
import requests
result = requests.get("https://data.cityofchicago.org/resource/6zsd-86xi.json?$where=date between '2024-01-10T12:01:00' and'2024-01-10T12:10:00'")
print(result.json())
print(result.url)