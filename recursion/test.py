# def checkNumber(arr, x):
#     print(arr)
#     # Please add your code here
#     l=len(arr)
#     if l==0:
#         return "false"
#     if arr[0]==x:
#         return "true"
#     smallerList=arr[1:]
#     smallerListOutput=checkNumber(smallerList,x)
#     return smallerListOutput



# arr=[15,24,58,61,79,3,97,81,81,45,62,21,72,72,68,45,11,50,87,20,28,77,51,89,58,66]
# x=26
# # print(checkNumber(arr,x))
# if checkNumber(arr, x):
#     print('true')
# else:
#     print('false')


def lastIndex(a,x,si):
    l=len(a)
    if si==l:
        return -1
    smallerlistOutput=lastIndex(a,x,si+1)
    if smallerlistOutput != -1:
        return smallerlistOutput
    else:
        if a[si]==x:
            return si
        else:
            return -1
        
arr=[34,57,82,41,65,35,82,27,36,12,6,40,66,99,25,29,22,25,12,24,65,15,5,43,28,33,76,32,13,95,22,84,71,23,28,7,65,94,18,47,9,42,61,73]
x=61
si=0
print(lastIndex(arr,x,si))