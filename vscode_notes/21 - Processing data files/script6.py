import csv
results = [fields for fields in csv.reader(open('temp_data_01.csv',newline=""))]
print(results)