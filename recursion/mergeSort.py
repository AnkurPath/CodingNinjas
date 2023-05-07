# Merge Sort Code
# Send Feedback
# Given the starting 'l' and the ending 'r' positions of the array 'ARR', your task is sorting the elements between 'l' and 'r'.
# Note:
# Change in the input array itself. So no need to return or print anything.
# Example:
# Input: ‘N’ = 7,
# 'ARR' = [2, 13, 4, 1, 3, 6, 28]

# Output: [1 2 3 4 6 13 28]

# Explanation: After applying 'merge sort' on the input array, the output is [1 2 3 4 6 13 28].
# Input format :
# The first line contains an integer 'N' representing the size of the array/list.

# The second line contains 'N' single space-separated integers representing the elements in the array/list.
# Output format :
# You don't need to return anything. In the output, you will see the array after modification is done by you.
# Constraints :
# 1 <= N <= 10^3
# 0 <= ARR[i] <= 10^9
# Sample Input 1:
# 7
# 2 13 4 1 3 6 28
# Sample Output 1:
# 1 2 3 4 6 13 28
# Explanation of Sample Output 1:
# After applying 'merge sort' on the input array, the output is [1 2 3 4 6 13 28].
# Sample Input 2:
# 5
# 9 3 6 2 0
# Sample Output 2:
# 0 2 3 6 9
# Explanation of Sample Output 2:
# After applying 'merge sort' on the input array, the output is [0 2 3 6 9].


def merge(arr: [int], l:int, m: int, r: int):
    num1=m-l+1
    num2=r-m

    L=[None]*num1
    R=[None]*num2

    for i in range(num1):
        L[i] = arr[l + i]

    for j in range(num2):
        R[j]=arr[m+j+1]

    i=0
    j=0
    k=l
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            arr[k]=L[i]
            i=i+1
        else:
            arr[k]=R[j]
            j=j+1
        k=k+1
    while i < len(L):
        arr[k]=L[i]
        k=k+1
        i=i+1
    while j < len(R):
        arr[k]=R[j]
        k=k+1
        j=j+1

    



def mergeSort(arr: [int], l: int, r: int):
    if l < r:
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)




