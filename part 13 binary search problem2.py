'''
Input : Sorted array of n elements and target sum
Output : Find any 2 element such that the sum of those two elements is equal to the target sum.
For example : 
array =[2,7,11,15] target = 9
The pair is 2 and 7
Solution :
time complexity:
linear search:
N * LS(n) = O(n^2)
binary search:
N * BS(n) = O(n logn)
Greedy algorithm = O(n) 
'''
#code : linear search
def findpairls(arr,targetsum):
   
    for i in range(len(arr)):
        n=i
        for j in range(i+1,len(arr)):
            if arr[n]+arr[j]==targetsum:
              return (arr[n],arr[j]) 
    return -1
arr=[2,7,11,15]
targetsum=9
result=findpairls(arr,targetsum)
print(result)

#code: binary search

def findpairbs(arr,targetsum,i,j):
   for k in range(len(arr)):
    n=k 
    while(i<=j):
       
        mid=(i+j)//2
        if arr[mid]+arr[n]==targetsum:
           return (arr[n],arr[mid])
            
        elif arr[mid]+arr[n]>targetsum:
            j=mid-1
        else:
            i=mid+1   
arrbs=[2,7,11,15]
targetsumbs=9
l=findpairbs(arrbs,targetsumbs,1,len(arr)-1)
print(l)

#code : greedy algorithm

def findpairgredalg(arrgd,targetsumgd,i,j):
    while(arrgd[i]+arrgd[j]!=targetsumgd):
        if(arrgd[i]+arrgd[j]>targetsumgd):
            j=j-1
        else:
            i=i+1
    return(arr[i],arr[j])
arrgd=[2,7,11,15]
targetsumgd=9

pairindex=findpairgredalg(arrbs,targetsumgd,0,len(arr)-1)
print(pairindex)
