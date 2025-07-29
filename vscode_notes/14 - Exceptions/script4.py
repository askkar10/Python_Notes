# error gdzie nie mozna dzielic przez o
x = int(input("Please enter an integer: "))
y = int(input("Please enter an integer: "))

try: 
  z = x/y
except ZeroDivisionError as e:
  print("Can't divide by 0")
finally:
  print(z)