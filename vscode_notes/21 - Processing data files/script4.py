line = "Illinois|1979/01/01|17.48|994"
print(line.split("|"))

result = []
for line in open('temp_data_pipes_00a.txt'):
    field = line.strip().split("|")
    result.append(field)

print(result)