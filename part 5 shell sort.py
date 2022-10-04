def shellsort(arr):
    gap=len(arr)//2
    while(gap>0):
        for i in range(gap,n):
            value=arr[i]
            j=i
            while j>=gap and arr[j]<arr[j-gap]: # arr[j] is same as value
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=value
        gap=gap//2
    return arr



n=int(input("enter size"))
arr=[int(input("enter a no")) for i in range(n)]    
result=shellsort(arr)
print(result)