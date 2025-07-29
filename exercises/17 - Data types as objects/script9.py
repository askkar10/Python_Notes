from collections import UserList
class TypedUserList(UserList):
    def __init__(self,example_element,initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list,list):
            raise IndexError("It'is not a list")
        for element in initial_list:
            self.__check(element)
        super().__init__(initial_list)
    def __check(self,element):
        if type(element) != self.type:
            raise IndexError('This is not this type')
    def __setitem__(self,i,element):
        self.__check(element)
        self.data[i] = element
    def __getitem__(self,i):
        return self.data[i]
    
x = TypedUserList("",5*[""])
print(x)
x[2] = 'Hello'
x[4] = 'there'
print(x[:])
x.sort()
del x[4]
print(x[:])