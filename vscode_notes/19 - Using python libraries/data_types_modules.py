# datetime, calendar -> date time and calendar operations
import datetime,calendar
from datetime import timedelta
year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23,
                         minutes=50, seconds=600)
year == another_year
print(year.total_seconds())

import calendar
print(list(calendar.day_name))

# collections -> container data types
import collections
x = 'askaniusz'
x = collections.Counter(list(x))
print(x)

# enum -> allows creation of enumerator classes that binds symbolic names to constant values
from enum import Enum

# class syntax
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# functional syntax
Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])
print(Color(1),Color(2),Color(3))

# sched -> event scheuler

# array -> efficent arrays of numeric values
from array import *
array_num = array('i', [1,3,5,7,9])
print(array_num.typecode)
print(array_num.itemsize)

# queye -> synchronized queue class

import threading
import queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
for item in range(30):
    q.put(item)

# Block until all tasks are done.
q.join()
print('All work completed')

# copy -> shallow and deep copy operations
import copy
a = [[1],[2],[3]]
b = copy.copy(a)
print(b)

# pprint -> data pretty printer

import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff)
pprint.pp(stuff)

# typing -> support for annotating code with hints as to the types of objects, particulary of funcion parameteers and return values

from typing import List

# Vector is a list of float values
Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

a = scale(scalar=2.0, vector=[1.0, 2.0, 3.0])
print(a)