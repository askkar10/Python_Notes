# struct module -> rading and writing binary data
import struct
record_format = 'hd7s'
data_record = struct.pack(record_format, 42, 3.14, b'goodbye')
with open("data", "wb") as data_file:
    data_file.write(data_record)
# h -> single c short integet
# d -> single c double precision floating point
# s -> string
# 7s -> string zawierajacy 7 znaków