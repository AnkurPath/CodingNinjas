import time


# find first presence the given value in a list(print index also)


#Approach -1 
##_______________________creating a new list

def findIndex1(a,x):
    l=len(a)
    if l==0:
        return -1
    if a[0]==x:
        return 0
    smallerlist=a[1:]
    smallerlistOutput=findIndex1(smallerlist,x)
    if smallerlistOutput==-1:
        return -1
    else:
        return smallerlistOutput + 1
    

#Approach 2
##_____________________________without creating new list
def findIndex2(a,x,start_index):
    l=len(a)
    if start_index==l:
        return -1
    if a[start_index]==x:
        return start_index

    smallerlistOutput=findIndex2(a,x,start_index+1)
    return smallerlistOutput



a=[1,2,6,4,5,8,97,23,56]
x=10
# start=time.perf_counter()
# print(findIndex1(a,x))
# mid=time.perf_counter()
# print(findIndex2(a,x,0))
# end=time.perf_counter()
# print("for index1",mid-start)
# print("for index2",end-start)