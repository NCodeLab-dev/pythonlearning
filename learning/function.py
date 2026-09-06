#functions in python

#readability
#maintainalibity
#reusuability
#modularity

def printMyname(name):
    print("Pallavi kanduri ta au ta daka na hela",name)

printMyname("richa")

'''
print("jane kanduri ta au ta daka na hela richa")
print("jane kanduri ta au ta daka na hela Alok")
print("jane kanduri ta au ta daka na hela jackson")
print("jane kanduri ta au ta daka na hela bibhu")
print("jane kanduri ta au ta daka na hela Pallavi")
'''


def add(x=1,y=1):
    return x+y;



print(add(y=6,x=4));



print(add())

def printSahuFamilyNames(name,title="Sahu"):
    print("family member",name,title)

printSahuFamilyNames(name="Pramod Kumar")
printSahuFamilyNames("sanket")
printSahuFamilyNames("pallavi")
printSahuFamilyNames("Bijayalaxmi", "Mahapatra")


tuple_type = (4,"five",6)
dict_type = {
    1: "One",
    2: "Two",
    "Three": 3
}

"""
*  -> used for passing tuple as a parameter
** -> used for passing dictionary as a parameter
"""

def printTupleOrDict(*t,**d):
    for x in t:
        print("printing tuple: ",x)
    print("-----------------------")
    for y in d:
        print("hello",d[y])


printTupleOrDict(4, "five", six=6, first="One",
                 second= "Two",
                 third= 3)

print("----------------------------------")
#funcion within function

def fun1():
    print("inside function one")
    def fun2():
        print("inside function two")
    fun2()

fun1()
print("----")


def funOne(x):
    x = 10;

y = 20;
funOne(y);
print(y);
#because x or y is immutable

def funList(l):
    l[0]=10;

list_type = [1,2,3,4,5,6];
funList(list_type);
print(list_type)

#list is mutuable

#pass keyword in function

def functionf():
    pass
    print("After pass")

functionf()

print("program end")
print("-------------")

#pass keyword in condition

day = "Monday"
if day == "Saturday":
    print("yes i will do my work")
elif day == "Sunday":
    pass
else:
    print("Already working day")


#pass keyword in loops

#print even numbers in all single digits
singledigitNumbers = range(0, 10) # 0-> 9
for x in singledigitNumbers:
    if(x%2!=0):
        pass
    else:
        print(x)