# 'rb' -> binary mode
input_file = open('binary-output.txt','rb')
header = input_file.read(4)
data = input_file.read()
input_file.close()
print(header)
print(data)