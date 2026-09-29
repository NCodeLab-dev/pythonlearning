
"""
# write a program to display all the natural numbers from 1 to n. (n is user input)
user_input = int(input("Please enter a number "))

for i in range(1, user_input+1):
    print(i)

# Write a program to display all natural numbers from 1 to n in reverse order.

for i in range(user_input,0,-1):
    print(i)
"""
user_input = int(input("please enter a number"))

"""
# Write a program to display all even numbers from 1 to n.

for i in range(1,user_input+1):
    if i%2==0:
        print("even",i)
    else:
        print("odd",i)
"""

# Write a program to find the sum of all natural numbers from 1 to n
"""
sum =0;
even_sum =0;
odd_sum =0;
for i in range(1,user_input):
    if i%2 ==0:
        even_sum=even_sum+i;
    else:
        odd_sum=odd_sum+i;
    sum =sum+i
print("sum is :",sum)
print("sum of evens:",even_sum)
print("sum of odds:",odd_sum)
"""

"""
# Write a program to find the product of all natural numbers from 1 to n (factorial of n).
product=1;
for i in range(1, user_input):
    product=product*i
print(f"""#factorial of {user_input} is """,product)
#"""

# Write a program to display the multiplication table of a number n.

"""
for i in range(1,11):
    print(f"{user_input}*{i}={user_input*i}")
"""

# Write a program to display all multiples of a number m up to n terms.

"""
m = int(input("enter a number"));
for i in range(1,user_input+1):
    print(m*i)
"""

"""
# Write a program to count how many numbers from 1 to n are divisible by 3.

count= 0;
for i in range(1,user_input):
    if i%3 ==0:
        count+=1;
print("numbers divisible by 3 are ",count)
"""

# Write a program to display all numbers from 1 to n that are divisible by 3 or 5.

for i in range(1, user_input+1):
    if i % 3 == 0 or i %5 ==0:
        print("numbers divisible by 3 or 5 are",i)

