# otwieranie takiego pliku
import struct
record_format = 'hd7s'
record_size = struct.calcsize(record_format) # calsize to otwieranie takich plików
result_list = []
with open('data','rb') as input:
  while True:
    record = input.read(record_size)
    if not record:
      break
    result_list.append(struct.unpack(record_format,record))
print(result_list)