bikes = ["Honda", "suzuki", "Bajaj", "apache",
         "royal enfield", "yamaha", 1, 2, 3]
# <class 'list'> ordered of collections of things of different types
print(type(bikes))

print(bikes[0])

# check if an item present or not
print("Honda" in bikes)  # True
print("Maruti" in bikes)  # false

print(len(bikes)); #9

languages = []

languages.append("python")
languages.append("java")
removed_lang = languages.pop() #removes java
print(languages) # java
print(removed_lang)

print(bikes[0],bikes[1]) # zero based indexing

print(bikes[len(bikes)-1]) #last item
print(bikes[-1]) # last item


# slicing a list in python

print(bikes)

print(bikes[0:3])#['Honda', 'suzuki', 'Bajaj']
sliced_list = bikes[1:3]
print(sliced_list)  # ['suzuki', 'Bajaj']

print(bikes[:3])  # ['Honda', 'suzuki', 'Bajaj']
print(bikes[3:])  # ['apache', 'royal enfield', 'yamaha', 1, 2, 3]
print(bikes[:3]+bikes[3:]) # ['Honda', 'suzuki', 'Bajaj', 'apache', 'royal enfield', 'yamaha', 1, 2, 3]

print(bikes[::1])  # ['Honda', 'suzuki', 'Bajaj', 'apache', 'royal enfield', 'yamaha', 1, 2, 3]
# this prints all
#first one is start index defaults to 0: second one to till index defaults to len(list): last one is step which is by default 1
print(bikes[::2])  # ['Honda', 'Bajaj', 'royal enfield', 1, 3] skips one index

#print(bikes[::0])  # error ValueError: slice step cannot be zero

#putting -1 reverses a list
print(bikes[::-1]) #[3, 2, 1, 'yamaha', 'royal enfield', 'apache', 'Bajaj', 'suzuki', 'Honda']

#print first 3 items

print("printing first 3 items:", bikes[:3]) # printing first 3 items: ['Honda', 'suzuki', 'Bajaj']

#printing last 3 items

print("printing last 3 items:", bikes[-3:])  # printing last 3 items: [1, 2, 3]

# print all items except first and last one

print(bikes[1:-1])  # ['suzuki', 'Bajaj', 'apache', 'royal enfield', 'yamaha', 1, 2]



print("---------------------------------------------")

#looping through a list 

# list is iterable
for bike in bikes:
    print(bike)

#such as string is also iterable

for char in "hello world":
    print(char)

#sequences

# list and string are both iterable as well as sequences because 
# 1. we can run for loop which makes it iterable
# 2. we can run using indexes which makes it a sequence
# But
# for example set is not a sequence althogh it's iterable
# 
# all iterables are sequences but all sequences are not iterable

set_xample = {1,2,3,4,5}

# we can print using iterables

for i in set_xample:
    print(i);

# but we can access using indexes
# print(set_xample[0])  # TypeError: 'set' object is not subscriptable

# rolling dice example, a dice has 6 sides

#lets take command line input 

print("---------------------------------------------")

import sys
from random import randint

# check for the lengh of argv, is value is not passed then make it default as 6

if len(sys.argv) == 1:
    sides = 6;
else:
    sides = sys.argv[1]
print(randint(1,int(sides)))


