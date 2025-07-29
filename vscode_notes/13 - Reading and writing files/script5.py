# writeline zapisuje szereg róznych linii
input_file = open('moby_dick.txt','r',encoding='utf-8')
lines = input_file.readlines()
input_file.close()
output = open('moby_dick2.txt','w',encoding='utf-8')
output.writelines(lines)
output.close()