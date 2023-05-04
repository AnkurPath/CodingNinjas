# print numbers from 1 to n(given by user) using Recursion
def printfirst_n(n):
    if n==0:
        return
    printfirst_n(n-1)
    print(n)
    return

print(printfirst_n(10))
