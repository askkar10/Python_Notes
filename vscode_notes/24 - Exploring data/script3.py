# data aggregation and manipulation
# merging data frames (łączenie)
import pandas as pd

calls = pd.read_csv("sales_calls.csv")
revenue = pd.read_csv("sales_revenue.csv")
# print(calls)
# print(revenue)

# merge to data frames 
calls_revenue = pd.merge(calls,revenue, on=['Territory','Month'])
# print(calls_revenue)

# lookin at 'territory' = 3
# print(calls_revenue[calls_revenue.Territory==3])

# select only rows in which the amount per call is greater than 500
# print(calls_revenue[calls_revenue.Amount/calls_revenue.Calls>500])

# you can calculate and add that column to your data frame
calls_revenue['Call_Amount'] = calls_revenue.Amount/calls_revenue.Calls
# print(calls_revenue)

# grouping and aggregation
# sum,mean(średnia arytmetyczna),median,minimum and maximum values
# print(calls_revenue.Calls.sum())
# print(calls_revenue.Calls.mean())
# print(calls_revenue.Calls.median())
# print(calls_revenue.Calls.max())
# print(calls_revenue.Calls.min())

# if you want to get all of the rows in which the amount per call is above the median,
# you can combine this thick with the selection operation

# print(calls_revenue.Call_Amount.median())
# print(calls_revenue[calls_revenue.Call_Amount >= calls_revenue.Call_Amount.median()])

# "groupby()" method to grouping your data 
# you may want to know the total calls and amounts by month or by territory
# print(calls_revenue[['Month','Calls','Amount']].groupby(['Month']).sum())
# print(calls_revenue[['Territory','Calls','Amount']].groupby('Territory').sum())

# plotting data (wizaualizacja danych)
import matplotlib
print(calls_revenue[['Territory','Calls','Amount']].groupby('Territory').sum().plot.line())

