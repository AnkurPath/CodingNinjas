# Quick Sort Code
# Send Feedback
# Sort an array A using Quick Sort.
# Change in the input array itself. So no need to return or print anything.


# Input format :
# Line 1 : Integer n i.e. Array size
# Line 2 : Array elements (separated by space)
# Output format :
# Array elements in increasing order (separated by space)
# Constraints :
# 1 <= n <= 10^3
# Sample Input 1 :
# 6 
# 2 6 8 5 4 3
# Sample Output 1 :
# 2 3 4 5 6 8
# Sample Input 2 :
# 5
# 1 2 3 5 7
# Sample Output 2 :
# 1 2 3 5 7 



def partitionArray(input: [int], start: int, end: int) -> int:
    # Take the first element as the pivot
    pivot = input[start]
    
    # Initialize the indices for the two subarrays
    i = start + 1
    j = end
    
    while True:
        # Move the left index i to the right until input[i] >= pivot
        while i <= j and input[i] < pivot:
            i += 1
        
        # Move the right index j to the left until input[j] <= pivot
        while i <= j and input[j] > pivot:
            j -= 1
        
        if i >= j:
            # The indices have crossed, so the partition is complete
            break
        
        # Swap the elements at input[i] and input[j]
        input[i], input[j] = input[j], input[i]
        
        # Move both indices inward
        i += 1
        j -= 1
    
    # Swap the pivot element with the element at index j
    input[start], input[j] = input[j], input[start]
    
    # Return the index of the pivot element
    return j


def quickSort(arr, start, end):
    if start < end:
        # Partition the array and get the index of the pivot element
        pivotIndex = partitionArray(arr, start, end)
        
        # Recursively sort the subarrays to the left and right of the pivot
        quickSort(arr, start, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, end)



