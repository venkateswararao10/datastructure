
## Method definition for merge procedure 
## Combine
def mergeProcedure(arr, i, mid, j):
    n1 = mid - i + 1
    n2 = j - (mid+1)+1

    arr1 = [0] * n1
    arr2 = [0] * n2

    for m in range(n1):
        arr1[m] = arr[i+m]
    
    for q in range(n2):
        arr2[q] = arr[mid+1+q]

    p = 0
    q = 0
    k = i

    while p < n1 and q < n2:
        if arr1[p] < arr2[q]:
            arr[k] = arr1[p]
            p += 1
        else:
            arr[k] = arr2[q]
            q += 1
        k += 1
    
    while p < n1:
        arr[k] = arr1[p]
        p += 1
        k += 1
    
    while q < n2:
        arr[k] = arr2[q]
        q += 1
        k += 1
        
## Method definition for mergeSort algorithm
def mergeSort(arr, i, j):
    if i < j:
        ## Divide
        mid = i + (j-i)//2
        ## Conquer
        mergeSort(arr, i, mid)
        mergeSort(arr, mid+1, j)
        ## Combine
        mergeProcedure(arr, i, mid, j)
    return arr

## Driver code
arr = [50, 20, 40, 90, 88, 11, 13]
n = len(arr)
result = mergeSort(arr, 0, n-1)
print("Sorted array after applying merge sort is:", result)