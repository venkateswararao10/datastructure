'''
Problems Discussion on Binary Search

Input - An array of n-elements in which until some place all are integers and afterwards all are infinite.
Output - Find the position of first infinite element.
Logic : Don’t see that an array is physically sorted or not. 
Think about the array logically also. If we can go to middle position 
and can not able to decide that whether to go for left hand side or to go for right hand side in an array, 
then Binary Search can not be possible in that problems irrespective of whether the array is unsorted or sorted.
time complexity: 
Linear Search - O(n)
Binary Search - O(logn) 
'''

#code : recursive approach
def pos_of_firstinfele(arr,target,i,j):
    if i>j:
        return -1
    else:
        mid=(i+j)//2
        if arr[mid]==target:
            if arr[mid-1]==target:
               return pos_of_firstinfele(arr, target, i, mid-1)
            return(mid)
        else:
           return pos_of_firstinfele(arr, target,mid+1,j)
            

arr=[12,32,45,23,9,77,54,99,89,76,56,90,"infinite","infinite","infinite"]
target = "infinite"
posi=pos_of_firstinfele(arr,target,0,len(arr)-1)
print(posi)

# linear search

def findpos(arr):
 for i in range(len(arr)):
    if arr[i]=="infinite":
        return i
arr=[12,32,45,23,9,77,54,99,89,76,56,90,"infinite","infinite"]
pos=findpos(arr)
print(pos)
