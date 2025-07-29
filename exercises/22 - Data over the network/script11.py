import requests
import xmltodict
response = requests.get('https://api.worldbank.org/v2/country/CL/indicator/SP.POP.TOTL?format=xml')
pop_data = response.text[3:]
population = xmltodict.parse(pop_data)
print(population)