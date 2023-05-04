# here we are working on fibonacci series with Recursion
# n= nth fibonacci number

def fib(n):
    if n==1 or n==2:
        return 1
    fib_first_previous=fib(n-1)
    fib_second_previous=fib(n-2)
    number=fib_first_previous+fib_second_previous
    return number

print(fib(6))


