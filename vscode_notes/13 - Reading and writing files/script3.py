file_object = open('myfile.txt','r')
line = file_object.readline()
print(line)
# ...... tutaj mozemy wyegzekwować nasz kod
file_object.close
# r -> otworzenie pliku to odczytania
# w -> otworzenie pliku do zapisania i napisania czegos tam
# a -> otworzenie pliku do dodania

file_object = open('myfile2.txt','w')
file_object.write('Hello, World\n')
file_object.close()