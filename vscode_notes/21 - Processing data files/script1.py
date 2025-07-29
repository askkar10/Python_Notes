# utf-8 encoding is best for reading text files
# open('test.txt','wb').write(bytes([65,66,67,255,192,193]))

# x = open('test.txt').read();print(x)

print(open('test.txt',errors='ignore').read())
print(open('test.txt',errors='replace').read())
print(open('test.txt',errors='surrogateescape').read())
print(open('test.txt',errors='backlashreplace').read())