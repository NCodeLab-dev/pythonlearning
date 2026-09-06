# Write a program to print "Hello, World!" on the screen.
'''
print("Hello world");
'''

'''

# Write a program to read two numbers and print their sum.

print("addition:-",int(input("Enter first number"))+int(input("Enter second number")))

# Write a program to read two numbers and print their sum, difference, product and quotient.

print("diff:-",int(input("Enter first number"))-int(input("Enter second number")))

# Write a program to read the radius of a circle and print its area and circumference.


radius = int(input("Please enter the raduis"))
print("Area: ",22/7*(radius*radius));
print("circumference: ",2*22/7*radius)

# Write a program to read the length and breadth of a rectangle and print its area and perimeter.

length=int(input("Enter length"));
breadth=int(input("Enter breadth"));

print("Area:",length*breadth);
print("perimeter:",(length+breadth)/2);
'''

# Write a program to swap two numbers using a third variable.
'''
x = int(input("Enter first num"));
y = int(input("Enter second num"));

z=x;
x=y;
y=z;

print(x,y)
'''

# Write a program to swap two numbers without using a third variable.
'''
x = int(input("Enter first num"))
y = int(input("Enter second num"))

x,y=y,x

print(x,y)
'''

# Write a program to read a temperature in Celsius and convert it to Fahrenheit.

'''
temp=int(input("enter tempetrature"))

print("temp in F", (temp*1.8)+32);
'''

# Write a program to read the marks of 5 subjects and print the total and average.

'''
math = 99;
physics = 92;
chem = 89;
bio = 86;
eng = 82;
total = math+physics+chem+bio+eng;
print("Total: ", total)
print("Average: ",(total)/5)
'''


# Write a program to read seconds and convert them into hours, minutes and seconds.


seconds = int(input("Enter time"));

minutes = seconds/60;
leftSeconds = seconds%60;

hours = minutes/60;
leftminutes = minutes%60;

print("hours:",int(hours));
print("minutes:", int(leftminutes))
print("seconds:", int(leftSeconds))




