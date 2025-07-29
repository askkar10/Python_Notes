import struct

record_format = 'hd7s'
record_size = struct.calcsize(record_format)
result_list = []
with open("struc_binary", 'rb') as input:
    while True:
        record = input.read(record_size) 
        if not record:  
            break
        result_list.append(struct.unpack(record_format, record))  #C

print(result_list)
     