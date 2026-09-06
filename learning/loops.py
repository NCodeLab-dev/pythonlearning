

#for loop
'''
list_type = [1,2,3,4,5]

for i in list_type:
    print(i)
'''

#range(first_number, till_last_number, jump ) in python

x = range(4,10,2)

#for i in x:
#    print(i)


list_type = [1, 2, 3, 4, 5]

print(len(list_type))

for i in range(len(list_type)):
    print(list_type[i])


number = 1;

while (number <= 15):
    print(number)
    number+=1;
print("-----")
print(number)

print("--------")

print("Narayan",end=" ")
print("sahu")

#print pattern

"""
1 
2 2 
3 3 3 
4 4 4 4 
"""

for i in range(1,5):
    for j in range(i):
        print(i)

