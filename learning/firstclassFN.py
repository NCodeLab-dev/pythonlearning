

def add(x,y):
    print("addition is :",x+y);


def mix(a,b,function):
    return function (a,b)

mix(7,8,add)

#create a dictionary of math functions

def add(x,y):
    return x+y;

def substact(x,y):
    return x-y;

def multi(x,y):
    return x*y;

def divison(x,y):
    return x/y;

dict_math = {
    "add":add,
    "sub": substact,
    "multi": multi,
    "div":divison
}

print(dict_math["add"](4,5))
print(dict_math["sub"](4, 5))
print(dict_math["multi"](4, 5))
print(dict_math["div"](4, 5))
