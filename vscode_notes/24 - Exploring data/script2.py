# loading and saving data with pandas
# text files, spreadsheets, JSON, XML, HTML
# sql databases -> google bigquery, hdf

import pandas as pd
import numpy as np

# reading JSON file using pandas
mars = pd.read_json("mars_data_01.json")
# print(mars)

# reading a CSV file
temp = pd.read_csv("temp_data_01.csv")
# print(temp)
temp = pd.read_csv("temp_data_01.csv", header=0, names=range(18), usecols=range(4,18))
# print(temp)

# converting 'missing' value to NaN
temp = pd.read_csv("temp_data_01.csv", na_values=["Missing"])
# print(temp)

# SAVING DATA
grid = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(grid,columns=["one","two","three"])
df.to_csv("df_out.csv", index=False)
# setting idndex to "False" means that the row indexes will to be written

# you can transform a data grid to a JSON object or write it to a file
df.to_json("df_out.json")
# supplying a file path as an argument writes the JSON to that file rather than returning it

# data cleaning with a data frame
temp = pd.read_csv("temp_data_01.csv", na_values=["Missing"], header=0,
                   names=range(18),usecols=range(4,18))
# print(temp)
# setting header=0 turns of the header for columns labels

# value of column 17
# print(temp[17][0]) # is a string

# to fix this problem u need: remove the % from the end of the value and then cast the value from a string to number
# temp[17] = temp[17].str.strip("%")
# print(temp[17][0])
# temp[17] = pd.to_numeric(temp[17])
# print(temp[17])
# you can use the "div()" method to finish the job of turning those alues into fractions
# temp[17] = temp[17].div(100)
# print(temp[17])

# you can achieve the same result in a single line by cahining the three operators together
temp[17] = temp[17].str.strip("%")
temp[17] = pd.to_numeric(temp[17]).div(100)
print(temp[17])