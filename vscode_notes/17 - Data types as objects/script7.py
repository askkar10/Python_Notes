from ast import Index
class LineReader:
  def __init__(self,filename):
    self.fileobject = open(filename,'r') # opens file for reading
  def __getitem__(self,index):
    line = self.fileobject.readline() # read line
    if line == "": # if no more data .. 
      self.fileobject.close() # .. close fileboject ...
      raise IndexError # and raising error ...
    else:
      return line.split("::")[:2] # return split line, first two fields

# __getitem__() method - > we are enable instance of the class to be use as iterable in the for loop,
#  wchich reads a line of the file with each iteration