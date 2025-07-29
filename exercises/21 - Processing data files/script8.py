data = open('datafile').readlines()
data.sort()
print(data)

data.sort(key=str.lower)

data.sort(key=lambda x : x[5:])
print(data)

