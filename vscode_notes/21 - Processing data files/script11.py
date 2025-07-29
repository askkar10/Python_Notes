import csv
data = [{'State': 'Illinois',
 'Month Day, Year Code': '1979/01/01',
 'Avg Daily Max Air Temperature (F)': '17.48',
 'Record Count for Daily Max Air Temp (F)': '994'}]
fields = ['State', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)']
dict_writer = csv.DictWriter(open('temp_data_04.csv','w'), fieldnames=fields)
dict_writer.writeheader()
dict_writer.writerows(data)
del dict_writer