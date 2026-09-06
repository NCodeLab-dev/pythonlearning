

list_type = ['1','3','5','7']

result = map(int,list_type)
#print(list(result))
print(type(list(result)[0]))


print("-----------")


list_char = ["a","b","c","d","e"];

"""
def toUpper(char):
    return char.upper()

map(toUpper,list_char)

def map(fun,list):
    for i in list:
        fun(list[i])
        i= 0: toupper("a")
        i=1; toupper(b"")
"""

result1 = map(lambda char: char.upper(),list_char)

print(list(result1))

print("======")



list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]

def add(x,y):
    return x+y;


result = list(map(add,list_1,list_2))

print(result)
