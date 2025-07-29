# csv.DictReader
import csv
results = [fields for fields in csv.DictReader(open('temp_data_01.csv',newline=''))]
print(results[0])
print(results[0]['State'])