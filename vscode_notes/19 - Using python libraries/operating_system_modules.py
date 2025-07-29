# os -> miscellaneous operating system intarfaces

import os
cwd = os.getcwd()
print("Current working directory:", cwd)

# io -> core tools for working with streams

f = io.StringIO("some initial text data")

# time -> time access and conversions

import time
print(time.gmtime(0))

# optparse -> powerful command-line option parser

import optparse
parser = optparse.OptionParser()

# logging -> logging facility for python

import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("This will get logged.")

# getpass -> portable password input

# curses -> terminal handling for character-cell display

# platform -> acces to underlying platfrom's indetifying data
import platform
def get_like_distro():
    info = platform.freedesktop_os_release()
    ids = [info["ID"]]
    if "ID_LIKE" in info:
        # ids are space separated and ordered by precedence
        ids.extend(info["ID_LIKE"].split())
    return ids

# ctypes -> foreing function library for python 

from ctypes import *
print(windll.kernel32)
print(cdll.msvcrt)
libc = cdll.msvcrt

# select -> waiting for I/O completion

import select

# threading -> higher-level threading interface
import threading
import time

def crawl(link, delay=3):
    print(f"crawl started for {link}")
    time.sleep(delay)  # Blocking I/O (simulating a network request)
    print(f"crawl ended for {link}")

links = [
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]

# Start threads for each link
threads = []
for link in links:
    # Using `args` to pass positional arguments and `kwargs` for keyword arguments
    t = threading.Thread(target=crawl, args=(link,), kwargs={"delay": 2})
    threads.append(t)

# Start each thread
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# multiprocessing -> process-based threading interface

# importing the multiprocessing module
import multiprocessing

def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))

def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))

if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(10, ))
    p2 = multiprocessing.Process(target=print_cube, args=(10, ))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print("Done!")

# subprocess -> subprocess management

import subprocess
try:
    ans = subprocess.check_output(["python", "--version"], text=True)
    print(ans)

except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")