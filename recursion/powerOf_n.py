# here we are finding Power of given number using Recursion


def pow_n(n,x):
    if x==0:
        return 1
    elif n==0:
        return 0
    return n*pow_n(n,x-1)


print(pow_n(2,3))