

#recursion calling the same function again in such a way which reduces code complexity



def fun(i):
    print("fun called")
    i = i-1
    if i!=0:
        fun(i)

fun(8)

# print factorial function

def fact(n):
    if n == 0:
        return 1;
    else:
        return n * fact(n-1)

print(fact(5));

#fibo 0,1,1,2,3,5,8,13

def fibo(n):
    if n == 0:
        return 0;
    if n == 1:
        return 1;
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(13))
