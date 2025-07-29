# numbers -> numeric abstract base classes
import numbers

# math, cmath -> mathematical functions for real and complex numbers
import math,cmath
print(math.pi)
print(cmath.sqrt(16+1j))

# decimal -> decimal fixed-point and floating-point arithmetic

import decimal
float_division=4/3
decimal_devision=decimal.Decimal(4)/decimal.Decimal(3) 
print("Result for float division of 4 by 3:")
print(float_division)
print("Result for decimal division of 4 by 3:")
print(decimal_devision)

# statistics -> function for calculating mathematical staticstics

import statistics

grades = [85, 92, 83, 91]
weights = [0.20, 0.20, 0.30, 0.30]
print(statistics.fmean(grades, weights))

# fractions rational numbers
from fractions import Fraction
Fraction(16, -10)

# random -> generate pseudorandom numbers and choice and schuffle sequences

from random import choice,randint
print(randint(0,100))
x = ['askaniusz','michal','dawid']
print(choice(x))

# itertools -> functions that creates iterator for efficent looping

from itertools import count

for number in count(start=1, step=2):
    if number > 10:
        break
    print(number)

# functools -> higer-order functions and opeartions on calalble objects

from functools import partial

def power(a, b):
    return a ** b

pow2 = partial(power, b=2) 
pow4 = partial(power, b=4)  
power_of_5 = partial(power, 5) 

print(power(2, 3))    
print(pow2(4))       
print(pow4(3))       
print(power_of_5(2))  

print(pow2.func)     
print(pow2.keywords) 
print(power_of_5.args)

# operators -> standard operators as functions
import operator
print(operator.add(10,20))