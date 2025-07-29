import csv
data = [fields for fields in csv.DictReader(open('temp_data_01.csv',newline=""))]
print(data[1]['State'])