# Write a program to count the number of digits in a number n.
# Write a program to display all the digits of a number n (one per line).
# Write a program to find the sum of all digits of a number n.
# Write a program to find the product of all digits of a number n.
# Write a program to reverse a number n.

"""
user_input = int(input("please enter a number"))
count =0;
digits="";
sum =0;
product = 1;
while user_input !=0:
    last_digit = user_input % 10
    sum =sum +last_digit # sum of all digits
    product=product*last_digit # product of all digits
    digits = digits + str(last_digit); # showing all digits
    user_input=int(user_input/10)
    count =count+1;
print("digit count: ",count)
print("digit string: ",digits[::-1])
print("sum of digits: ",sum)
print("product of all digits",product)
print("reverse of all digits",digits)
"""



# Write a program to find the largest digit in a number n.

"""
user_input = int(input("please enter a number"))
max=0;
min=9;
count_even=0;
count_odd=0;
while user_input!=0:
    rem = user_input%10;
    if rem%2==0:
        count_even+=1;
    else:
        count_odd+=1;
    if rem>max:
        max = rem;
    if rem<min:
        min = rem
    user_input = int(user_input/10);
print("maximum digit is :", max)
print("minimum digit is :", min)
print("no of odd digit is :", count_odd)
print("no of even digit is :", count_even)
"""

# Write a program to check whether a number n is a palindrome (reads the same reversed).
"""
user_input = int(input("please enter a number"))

reverse=""
original = user_input
while user_input !=0:
    reverse=reverse+str(user_input%10);
    user_input=int(user_input/10);

if original == int(reverse):
    print("pallindrome")
else:
    print("not a pallindrome")
"""

"""
user_input=int(input("please enter a number"));

reverse="";
while user_input!=0:
    rem = user_input % 10;
    if rem == 5:
        rem=0
    reverse =reverse+ str(rem);
    user_input=int(user_input/10);

print(int(reverse[::-1]))
"""


# Write a program to find the sum of the first and last digit of a number n.
"""
user_input = int(input("please enter a number"))
count =0;
last_element=0;
first_element =0;
while user_input!=0:
    rem = user_input%10;
    if(count == 0):
        last_element = rem;
    count=count+1;
    user_input=int(user_input/10);
    if user_input ==0:
        first_element=rem;
    

print(last_element)
print(first_element)
print("sum of first and last element is: ",first_element+last_element)

"""


str1="Hello"
#print(str1[10])  # IndexError: string index out of range