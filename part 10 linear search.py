## Linear Search Algorithm Implementation
def LinearSearch(arr,x,n):
  for i in range(n):
    if (arr[i] == x):
      return i
  return -1   # -1 indicates that an element which you want 
                  #  to search is not present in an array
# Driver Code
arr = [53,21,90,32,47,89,90]
x = 100
n = len(arr)
#print(n)
result=LinearSearch(arr,x,n)
print(result)