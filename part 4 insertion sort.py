def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        value=arr[i]
        j=i-1
        while j>=0 and value<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=value
    return arr
l=eval(input("enter a list"))
result=insertionsort(l)
print(result)