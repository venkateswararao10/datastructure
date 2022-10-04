## Method Definition for the binary search
def binarySearch(arr, i, j, target):
    ## small problem -> one element in the array
    if i == j: # this if case is written r not no problem
        if arr[i] == target:
            return i
        else:
            return -1
    ## condition missing due to which error coming
    elif i > j:
        return -1
    ## big problem -> n >= 2
    else:
        mid = i + (j-i)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            ## right side of an array
            return binarySearch(arr, mid+1, j, target)
        else:
            ## left side of an array
            return binarySearch(arr, i, mid-1, target)
    return -1

## Driver code
arr = [10, 20, 30, 40, 50, 60, 70, 80]
target = 65
i = 0
j = len(arr) - 1
result = binarySearch(arr, i, j, target)
print("Searching element is present in the location:", result)

