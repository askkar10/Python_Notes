import os 
# C:\Users\askka\Desktop\python programs\13 - Reading and writing files
file_name = os.path.join('C:','Users','askka','Desktop','python programs','13 - Reading and writing files','test.txt')
print(file_name)
file_object = open(file_name,'r')
print(file_object.readline())
# nie wiem czemu ale cos nie chce zadziałać