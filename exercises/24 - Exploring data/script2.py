import pandas as pd
mars = pd.read_json("mars_data_01.json")
#print(mars)
temp = pd.read_csv("temp_data_01.csv")
#print(temp)
temp = pd.read_csv("temp_data_01.csv", na_values=['Missing'])
#print(temp)
temp = pd.read_csv("temp_data_01.csv", na_values=['Missing'], header=0,
                   names=range(18),usecols=range(4,18))
#print(temp)
print(temp[17][0])
temp[17] = temp[17].str.strip("%")
temp[17] = pd.to_numeric(temp[17]).div(100)
print(temp[17])