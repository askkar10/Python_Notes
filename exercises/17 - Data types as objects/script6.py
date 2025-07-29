class LineReader:
    def __init__(self,filename):
        self.objectname = open(filename,'r')
    def __getitem__(self,index):
        line = self.objectname.readline()
        if line == "":
            self.objectname.close()
            raise IndexError
        else:
            return line.split("::")

for name,surname in LineReader('pliczek.txt'):
    print(name,surname)