import csv
from openpyxl import Workbook
data_rows = [fields for fields in csv.reader(open('temp_data_01.csv'))]
wb = Workbook()
ws = wb.active
ws.title = 'temperature data'
for row in data_rows:
    ws.append(row)
wb.save('temp_data_02.xlsx')