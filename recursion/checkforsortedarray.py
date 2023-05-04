# An array or list will be given we have to check if arry is sorted or not with Recursion method


def isSorted(array,start_index):
    l=len(array)
    if start_index==l-1 or start_index==l:
        return True
    if array[start_index]>array[start_index+1]:
        return False
    isSmallerPartSorted=isSorted(array,start_index+1)
    return isSmallerPartSorted

print(isSorted([1,2,3,4,5,6],0))