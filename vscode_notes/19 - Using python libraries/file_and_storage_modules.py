# os.path -> perform common pathname manipulations
import os
out = os.path.basename("/baz/foo")
print(out)
# pathlib -> deal with pathnames in an object-oriented way
from pathlib import PurePath
obj = PurePath('foo/bar')
print(obj)
# fileinput -> iterate over lines from multiple input strams 
import fileinput
for line in fileinput.input(encoding="utf-8"):
    process(line)

# filecmp -> compare files an directories

# tempfile -> generate temporaru files and directories

# glob, fnmatch -> use UNIX-style pathname and filename pattern handling

# linecache -> gain random access to text lines

import linecache
linecache.getline(linecache.__file__, 8)

# shutil -> perform high-level file opartions

# Python program to explain shutil.copy() method 

# importing shutil module 
import shutil 

source = "path/main.py"
destination ="path/main2.py"

# Copy the content of 
# source to destination 
dest = shutil.copy(source, destination) 

# Print path of newly 
# created file 
print("Destination path:", dest) 

# pickle, shelve -> enable python object serialization and persisetence

import pickle

# initializing data to be stored in db
Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 
'age' : 21, 'pay' : 40000}
Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
'age' : 50, 'pay' : 50000}

# database
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish

# For storing
# type(b) gives <class 'bytes'>;
b = pickle.dumps(db)   

# For loading
myEntry = pickle.loads(b)
print(myEntry)

import shelve
shelve_file = shelve.open("gfg")


# sqlite3 -> work with DB-API 2.0 interface for SQLite dtabases

# zlib, gzip, bz2, zipfile, tarfile -> work with archive files and compressions

# csv -> read and write CSV files
import csv
with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

# configparser -> use a configuration file parser; read/wite Windows-style configuration .ini files

import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['forge.example'] = {}
config['forge.example']['User'] = 'hg'
config['topsecret.server.example'] = {}
topsecret = config['topsecret.server.example']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
  config.write(configfile)
