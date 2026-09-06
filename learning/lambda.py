



def printnum(num):
    print (num)


add = lambda num1,num2: (num1+num2)

print(add(5,6))


def check1(num):
    if num >0:
        print("+ve")
    elif num == 0:
        print("zero")
    else:
        print ("-ve")


check = lambda num : "Positive" if num>0 else "Negative" if num < 0 else "zero"

print(check(-45))


lambda arg=i:arg*10 for i in range(1,5)


function1 = []
