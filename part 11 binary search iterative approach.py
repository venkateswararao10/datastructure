## Binary Search - Iterative Approach
def BinarySearch(arr,low,high,x):
  while(low <= high):
    # Dividing the problem
    mid = low + (high - low)//2
    # if x is greater, ignore the left half
    if (arr[mid] < x):
      low = mid + 1
    # if x is smaller, ignore the right half
    elif (arr[mid] > x):
      high = mid - 1
    # x is present at the mid
    else:
      return mid
  # searched element not present in an array
  return -1

## Drive Code
arr = [2,5,7,12,34,56,79,80,90]
x = 90
n = len(arr)
pos = BinarySearch(arr,0,n-1,x)
print(pos)