with open('test.txt','r') as file_object:
  line = file_object.readline()
  print(line)
  file_object.close()