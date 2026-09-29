# Write a program to read a number and check whether it is prime or not .

user_input = int(input("Please enter a number "));


def is_prime(user_input):
    is_prime = True
    for i in range(2,user_input):
        if user_input%i ==0:
            is_prime=False
            break;
    return is_prime
print(is_prime(user_input))

# Write a program to display all prime numbers from 1 to n.

