# xml data
# fetching xml version of the world bank's population of chile
import requests 
result= requests.get("https://api.worldbank.org/v2/country/CL/indicator/SP.POP.TOTL?format=xml")
pop_data = result.text[3:]
print(pop_data)