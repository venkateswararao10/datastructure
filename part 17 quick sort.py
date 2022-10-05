def partition(arr,low,high): # arr = array,low = lower index of array, high = higher index of array
  '''
  partition function returns an index(i) between [low,high] and modifies the array 
  in such a way that, if arr[i]=v all elements with index lower than i will be less than or equal to v
  and all elements with index greater than i will be greater than v
  logic: we take pivot arr[low] = p,moving index(i) = low and pointer arr[low+1=j]=q as we increase j by one until we reach the end of array
  if arr[j]<=p we increment i by 1 and swap (arr[i],arr[j])
  after loop is completed we swap pivot with moving index element because we know all the elements upto moving index are less than or equal to pivot.
  Time Complexity : O(n) ,n= length of the input array that is n=high-low+1 and there is one loop in the function
  so and loop runs n times so time complexity is O(n)
  '''
  pivot = arr [low] #first element as pivot
  i = low # moving index
  for j in range(low+1,high+1):         #traversing the array to change ,high+1 as range function dosen't include last element
    if arr[j]<=pivot:                   # comparing with pivot and if it is less than or equal then swap it with moving index element
      i+=1                              #moving index increased by 1
      arr[i],arr[j]=arr[j],arr[i]       #swapping moving  index element  with arr[j]
  arr[i],arr[low]= arr[low],arr[i]      #swapping the pivot element with the moving index element
  return i                              #moving index
def quickSort(arr,low,high): # array = arr, low = lower index of array, high = higher index of array
  if high==low:# small problem  Time complexity : O(1)
    return arr
  elif low>high:
    return -1
  elif low<high:# if length of the array is not one
      m = partition(arr,low,high) #Time complexity O(n),where n = high-low+1
      quickSort(arr,low,m-1)      #T(m-low),m = partition index,left partition recursive call 
      quickSort(arr,m+1,high)     #T(high-m),m = partition index,right partition recursive call
  return arr
arr=[50,70,80,30,40,88,19,27,69]
result=quickSort(arr,0,8)

print(result)
