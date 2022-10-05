import random

def partitionrand(arr, p, q):
    pivot = random.randrange(p,q)
    arr[p], arr[pivot] = arr[pivot], arr[p]
    return partition(arr, p, q)

## Method definition for partition algorithm 
def partition(arr, p, q):
    pivot = arr[p]
    i = p
    for j in range(p+1, q+1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[p] = arr[p], arr[i]
    return i

## Method definition for quickSort
def quickSort(arr, i, j):
    ## Small Problem
    if i == j:
        return arr[i]
    elif j < i:
        return -1
    else:
        m = partitionrand(arr, i, j)
        quickSort(arr, i, m-1)
        quickSort(arr, m+1, j)
    return arr

## Driver code
arr = [50, 70, 80, 30, 40, 88, 19, 27, 69]  
result = quickSort(arr, 0, len(arr)-1)
print("Sorted array after applying quickSort is:", result)