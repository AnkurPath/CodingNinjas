# Sum Of Array
# Send Feedback
# Given an array of length N, you need to find and return the sum of all elements of the array.
# Do this recursively.
# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Output Format :
# Sum
# Constraints :
# 1 <= N <= 10^3
# Sample Input 1 :
# 3
# 9 8 9
# Sample Output 1 :
# 26
# Sample Input 2 :
# 3
# 4 2 1
# Sample Output 2 :
# 7    


def sumArray(arr):
    l=len(arr)
    if l==0:
        return 0
    smallerList=arr[1:]
    smallerListOutput=arr[0]+sumArray(smallerList)
    return smallerListOutput

    # Please add your code here
    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
