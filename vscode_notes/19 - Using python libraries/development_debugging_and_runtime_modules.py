# pydoc -> documentation generator and online help system
import pydoc
python -m pydoc sys

# doctest -> test interactive python examples
import doctest
doctest.testfile("example.txt")

# unittest -> unit testing framework
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

# test.support -> utility functions for test 
import unittest
from test import support

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        ... code to execute in preparation for tests ...

    def tearDown(self):
        ... code to execute to clean up after tests ...

    def test_feature_one(self):
        # Test feature one.
        ... testing code ...

    def test_feature_two(self):
        # Test feature two.
        ... testing code ...

    ... more test methods ...

class MyTestCase2(unittest.TestCase):
    ... same structure as MyTestCase1 ...

... more test classes ...

if __name__ == '__main__':
    unittest.main()

# pdb -> python debugger
import pdb
def f(x):
    print(1 / x)
pdb.run("f(2)")

# profile, cProfile => python profilers
import cProfile
import re
cProfile.run('re.compile("foo|bar")')

# timeit -> measure execution itme of small code snippets
import timeit
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

# trace -> trace or track python statement execution
import sys
import trace

# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.
tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=0,
    count=1)

# run the new command using the given tracer
tracer.run('main()')

# make a report, placing output in the current directory
r = tracer.results()
r.write_results(show_missing=True, coverdir=".")

# sys -> system-specific parameters and functions
import sys
sys.float_info.dig

s = '3.14159265358979'    # decimal string with 15 significant digits
format(float(s), '.15g')  # convert to float and back -> same value

# atexit -> exit handlers
def goodbye(name, adjective):
    print('Goodbye %s, it was %s to meet you.' % (name, adjective))

import atexit

atexit.register(goodbye, 'Donny', 'nice')
# or:
atexit.register(goodbye, adjective='nice', name='Donny')

# __future __ -> future statement definitions - features to be added to python

# gc -> garbage collector interface

# inspect -> inspect live objects
from inspect import signature
def foo(a, *, b:int, **kwargs):
    pass

sig = signature(foo)

str(sig)


str(sig.parameters['b'])


sig.parameters['b'].annotation

# zipimport -> import modules from zip archives

# modulefinder -> find modules user by a script
from modulefinder import ModuleFinder

finder = ModuleFinder()
finder.run_script('bacon.py')

print('Loaded modules:')
for name, mod in finder.modules.items():
    print('%s: ' % name, end='')
    print(','.join(list(mod.globalnames.keys())[:3]))

print('-'*50)
print('Modules not imported:')
print('\n'.join(finder.badmodules.keys()))