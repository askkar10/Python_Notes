import struct
record_format = 'hd7s'
data_record = struct.pack(record_format,3,3.14,b'siemano')
f = open('struc_binary','wb')
f.write(data_record)
f.close()