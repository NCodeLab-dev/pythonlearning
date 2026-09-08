
#tuple

#tuple is same as list but with one difference -> list is mutable and tuple is immutable

couple = ("Narayan","Pallavi") #tuple



groom,bride = couple; #tuple unpacking

print("groom:",groom) 
print("bride:", bride)


print(couple[0]+" Weds "+ couple[1]); # sequence data type

# couple[0] = "mg" # immutable

city =["bbsr","berhampur","bangalore"]

city[0] = "bhubaneswar"

print(city)

city_pin = ("bbsr",674)

#list of tuples


city = [("bbsr",674),("berhampur",761121),("bangalore",560078),(),()]


#city[0][0]="bhubaneswar" # immutable
#print(city[0][0])

state_capital = [("Odisha","BBSR"),("Karnataka","Bangalore"),("Maharastra","Mumbai")]


def XY():
    #this funtion will return co-ordinates
    return 1,2

print(type(XY()))






state_capital = [("Odisha", "BBSR"),("Karnataka","Bangalore"),("Maharastra","Mumbai")]


# print each state and it's capital using a function

def print_state_capital(state_capital):

    for each in state_capital:
        state,capital = each;
        print("---------------")
        print("State: ",state)
        print("capital: ", capital)
        print("---------------")

print_state_capital(state_capital)

#just like tuple we can also unpack the list

state_capital = [("Odisha", "BBSR"),("Karnataka","Bangalore"),("Maharastra","Mumbai")]

odia,kannada,marathi = state_capital

print(odia[0])
print(odia[1])
print(kannada[0])
print(kannada[1])
print(marathi[0])
print(marathi[1])

print(type(odia))

x = odia

tp = ("hello",1)

print(tp[0])
print(tp[1])