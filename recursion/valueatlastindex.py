# find last presence the given value in a list(print index also)
# Approach 1
# with making new list for each iteration
def lastIndex1(a,x):
    l=len(a)
    if l==0:
        return -1
    smallerList=a[1:]
    smallerListOutput=lastIndex1(smallerList,x)
    if smallerListOutput != -1:
        return smallerListOutput +1 
    else:
        if a[0]==x:
            return 0
        else:
            return -1

# Approach 2
# without making new list for each iteration 

def lastIndex2(a,x,si):
    l=len(a)
    if si==l:
        return -1
    smallerlistOutput=lastIndex2(a,x,si+1)
    if smallerlistOutput != -1:
        return smallerlistOutput
    else:
        if a[si]==x:
            return si
        else:
            return -1
    








a=[1,2,6,7,6,8,9,45,6,78,6,55,256]
x=6
print(lastIndex2(a,x,0))