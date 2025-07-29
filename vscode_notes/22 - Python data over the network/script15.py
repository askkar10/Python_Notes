# skipping extra characters
# 'xmltodict' -> simple data extraction, handest utility
# pip install xmltodict
import requests 
import xmltodict
result= requests.get("https://api.worldbank.org/v2/country/CL/indicator/SP.POP.TOTL?format=xml")
pop_data = result.text[3:]
population = xmltodict.parse(pop_data)
print(population)