# Write a program to read a number and check whether it is even or odd.
'''

num = int(input("Enter a num"));

if num%2==0:
    print("number is even");
else:
    print("number is odd");

'''


# Write a program to read a number and check whether it is positive, negative or zero.

"""
num = int(input("Enter a num"));

if num>0:
    print("number is positive");
elif num<0:
    print("number is negative");
else:
    print("number is zero");
"""

# Write a program to read three numbers and find the largest among them.
"""
first = 10;
second = 20;
third = 30

"""

# Write a program to read a year and check whether it is a leap year or not.

"""
year = 2000;

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")

"""

# Write a program to read a character and check whether it is a vowel or a consonant.


"""
char_input = input("Enter a char")

str="aeiouAEIOU"

if char_input in str:
    print("a vowel");
else:
    print("consonant");
"""
# Write a program to read a character and check whether it is an alphabet, digit or special
# symbol.

"""
inp=input("Enter a alphabet/digit/special symbol")

if inp.isdigit():
    print("it's a digit")
elif inp.isalpha():
    print("it's alphabet")
else:
    print("special symbol")
"""


# Write a program to read the marks of a student and print the grade(A/B/C/D/Fail).

"""
marks = int(input("enter marks"));

if(marks>=90):
    print("Grade A")
elif(marks>=80 and marks<90):
    print("Grade B")
elif(marks<80 and marks>70):
    print("Grade C")
elif(marks>40 and marks < 70):
    print("Grade D")
else:
    print("Fail ")
"""


# Write a program to read a number and check whether it is divisible by both 3 and 5.

"""
inp = int(input("enter a number"))
print("yes") if (inp % 3 ==0 and inp % 5==0) else print("No")
"""

# Write a program to read the age of a person and check whether they are eligible to vote.

age = int(input("Enter age"))

print("Eligible") if(age>=18) else print("Not eligible")
