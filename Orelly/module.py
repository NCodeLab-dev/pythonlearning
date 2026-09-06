# python standard library

import math

print(math.sqrt(25))  # 5.0

print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045
print(math)  # <module 'math' from '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload/math.cpython-313-darwin.so'>

#otherwise

from math import sqrt,e,pi

print(sqrt(25))  # 5.0
print(e, pi) #2.718281828459045 3.141592653589793

import Orelly.constants as constants # runs the constants.py hence runs print inside it
import Orelly.constants as constants # second time it doesn't print because it caches the module
#we see a __pycache__ folder in the same folder structure inside that we have a .pyc file
#this is created for user created modules not default modules
print(constants.message) # imported from other file


# we generally have functions and statements inside a module file to import it's functions 


print(input("Enter your name")); # we can get input from user and print

#we can also get command line argument using sys.argv

import sys

args = sys.argv;

print(args);  # ['/Users/narayan/Developer/languages/python/learning/Orelly/module.py', 'Hello']

print(args[1])