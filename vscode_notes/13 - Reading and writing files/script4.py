# readline -> return single line from a text
# liczenie ile linii ma plik - 3 sposoby

file_object = open('moby_dick.txt','r',encoding='UTF-8')
count = 0
while file_object.readline() != "":
  count = count + 1
print(count)
file_object.close()

file_object = open('moby_dick.txt','r',encoding='UTF-8')
count = 0
for line in file_object:
  count = count + 1
print(count)
file_object.close()

file_object = open('moby_dick.txt','r',encoding='utf-8')
lines = len(file_object.readlines())
print(lines)
file_object.close()