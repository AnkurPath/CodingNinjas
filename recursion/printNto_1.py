#print numbers from N(given by user) to 1 using Recursion

def printfirst_n(n):
    if n==0:
        return
    print(n)
    printfirst_n(n-1)
    return

print(printfirst_n(10))