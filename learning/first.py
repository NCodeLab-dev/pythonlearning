# in python3 print is a function in python2 it was not a function
print("This is my first python programme")

# multiline comments in python

"""
this is a multiline comment although the line is still in color
"""

x = 5
if x == 5:
    # indented four spaces
    print("yes, x is 5")
else:
    print("No, x is not 5")

# in python everything is an object
# Numbers 2 types:- integer and float

myint = 7
print(myint)  # 7
myfloat = 7.2
print(myfloat)  # 7.2
myint = float(myint)
print(myint)  # 7.0

print(float(3))  # 3.0

print('hello')
print('world')
print("don't use it")  # it has to be double quote

print("hello" + " "+"worls")
mystr = "narandrapur"
print("my village name is %s" % mystr)  # same as
print("my village name is ", mystr)
