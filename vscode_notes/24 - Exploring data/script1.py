# spreadsheet has row limit - abour 1 milions row

# why ou might to use pandas:
# * pandas was created for manipulating and analyzing tabular or relationala data easy by 
# providing a standard framework for hanlding the data

# installing pandas 
# pip install pandas
# pip install mantplotlib **** lub krótsza wersja "pip install pandas matplotlib"

#%mathplotlib inline
import pandas as pd
import numpy as np
# first line enables 'matplotlib' to plot data in cell where you code is, 
# the second line imports 'pandas' as 'pd, another is 'numpy' as 'np'

# data frames
# data frame is two-dimensional grid
grid = [[1,2,3],[4,5,6],[7,8,9]]
print(grid);print("---")

# for looking like a grid
df = pd.DataFrame(grid)
print(df);print("---")

# giving names for columns
df = pd.DataFrame(grid,columns=["one","two","three"])
print(df);print("---")

# printing only columnn two
print(df["two"]);print("---")

# list comprehension
print(list(x[1] for x in grid));print("---")

# looping over data
for x in df["two"]:
  print(x)
print("---")

# getting the dirst and last columns of your data frame as another data frame
edges = df[["one","three"]]
print(edges);print("---")

# addding 2 to every item in the frame edges, using "add()" method
print(edges.add(2));print("---")

print(df["two"].value_counts())