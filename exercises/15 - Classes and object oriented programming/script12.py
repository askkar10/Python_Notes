class Mine:
    def __init__(self):
        self.x = 2
        self.__y = 10
    def priv_y(self):
        print(self.__y)
    def __priv_method(self):
        print('Private method')
    def call_priv_method(self):
        self.__priv_method()

m = Mine()
print(m.x)
#print(m.__y)
m.priv_y()
m.call_priv_method()