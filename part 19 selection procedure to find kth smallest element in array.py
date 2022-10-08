def partition(arr,low,high):#arr = array,low=lower index,high= higher index
  pivot = arr[low]#first element as pivot
  i = low #moving index
  for j in range(low+1,high+1):#traversing the remaining elements to compare with pivot,high+1 as range function dosen't include last element,O(n)
    if arr[j]<=arr[low]:#comparing moving index element with pivot if it is less than or equal then we swap it with next element to moving index
      i+=1#moving index increased by 1
      arr[i],arr[j]=arr[j],arr[i]#swapping moving index element with arr[j]
  arr[low],arr[i]=arr[i],arr[low]#swapping moving index with pivot element
  return i 
def selectionProcedure(arr,low,high,k):#arr=array,low=lower index of array,high=higher index of array,k=kth smallest element in array to find
  if low==high:#small problem if arr lenght is one return the element,O(1)
    return arr[low]
  elif low>high:
    return -1
  else:
    m = partition(arr,low,high)                #Timecomplexity:O(length of array),O(high-low)
    if m == k:                             #Timecomplexity:O(1)
      return arr[m]                          #return the k th smallest element                               
    elif m<k:                                  # index is less than k then we move right side of array
      return selectionProcedure(arr,m+1,high,k)  #recursive call: T(high-m)
    else:
      return selectionProcedure(arr,low,m-1,k)   #recursive call: T(m-low)
array1=[50,75,35,25,80,90,120,110,11,21,31,51,79]
k=3
kthsmallestelement=selectionProcedure(array1,0,12,k-1)
print(kthsmallestelement)