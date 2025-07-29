a = [[1,2],[3,4]]
b = a[:]
a[0][0] = 10
print(a,b)
import copy
c = copy.deepcopy(a)
a[0][0] = 100
print(a,c)