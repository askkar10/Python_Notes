# normalnie byśmy musieli zamknąć plik i byłby długi kodzik
#try:
#  infile = open(filename,'r')
#  data = infile.read()
#finally:
#  infile.close()

# mozemy to zrobic szybciej

# mozemy to zrobić zdecydowanie szybciej
with open('moby_dick.txt','r',encoding='utf-8') as infile:
  data = infile.read()

print(data)