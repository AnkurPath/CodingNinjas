# find sum of n natural numbers using Recursion
def sumOf_n(n):
    if n==0:
        return 0
    return n + sumOf_n(n-1)

print(sumOf_n(5))