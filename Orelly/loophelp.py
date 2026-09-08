
#print 1 to 10 using range

for x in range(1,11,2):
    print(x)

for even in range(0,11,2):
    print(even)

for odd in range(0, 11, 2):
    print(odd)

# print 0-10
print("----")
for x in range(10,0,-1):
    print(x)

message = "python is a very good language"
print(message[0:30:2])

print(list(range(5,15,2))) # converting range return value to list

print("-------enumerate-------")


family = ["father","mother","sister","brother","grandfather","grandmother"]

"""
for member in family:
    print(member)

#usingg count
for member in range(len(family)):
    print(member+1,family[member])

"""


#enumerate is being used to provide a count of the given data/list
for count,member in enumerate(family,start =10):
    print(count,member)


