
import sys
def findMinandMax(arr, i, j, min = sys.maxsize, max = -sys.maxsize):
    ## single element
    if i == j:
        maxi = arr[i]
        mini = arr[i]
        return mini, maxi
    
    ## two element
    if i == j-1:
        if arr[i] < arr[j]:
            maxi = arr[j]
            mini = arr[i]
        else:
            maxi = arr[i]
            mini = arr[j]
        
        return mini, maxi
    ## big problem when n > 2
    ## 1. Divide
    mid = (i + j) // 2

    ##2. Conquer
    min1, max1 = findMinandMax(arr, i, mid, mini, maxi)
    min2, max2 = findMinandMax(arr, mid+1, j, mini, maxi)

    ## Combine 
    if min1 < min2:
        mini = min1
    else:
        mini = min2
    
    if max1 < max2:
        maxi = max2
    else:
        maxi = max1

    return mini, maxi

## Driver code
arr = [50, 90, 170, 25, 15, 7, 190, 4, 59]
n = len(arr)
(minim, maxim) = findMinandMax(arr, 0, n-1) 
print("The minimum element in the list is:", minim)
print("The maximum element in the list is:", maxim)