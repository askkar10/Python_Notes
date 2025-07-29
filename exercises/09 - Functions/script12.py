def func():
    i = 0
    while i < 4:
        yield i
        i+=1
    
for number in func():
    print(number)

print(2 in func())
print(5 in func())