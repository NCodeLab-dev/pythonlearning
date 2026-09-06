name ="pallavi" #input("Please enter your name")

'''
if name == "pallavi":
    print("I love you Pallavi");
else:
    print("Who are you?");
'''

print("I love you pallavi") if name == "pallavi" else print("who are you"); # without colon in one line

# eligible for vote or not also print senior citizen or not or teen or not

age = int(input("Enter your age\n"))
#print(type(age))
if age >18:
    print("Eligible for vote");
    if age >59:
        print("senior citizen")
    else:
        print("not senior citizen")
elif age >12:
    print("Teen age so go and apply ")
elif age<0:
    print("invalid age")
else:
    print("a kid go home")