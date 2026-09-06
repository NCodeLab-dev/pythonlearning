# global or local variable
name = "Pallavi"
def printPallavi():
    global name
    name += "Narayan"
    print(name)

printPallavi()
print(name)


if True:
    pass
    print("hello")
else:
    print("false")


"""
x = 10
def func():
    x = x + 1   # Trying to modify x # error


func()
"""

