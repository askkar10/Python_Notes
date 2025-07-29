import csv
data = [fields for fields in csv.reader(open('temp_data_pipes_00a.txt',newline=""),delimiter='|')]
print(data)