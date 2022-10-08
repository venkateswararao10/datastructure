def mergeSort(arr,n):
    temparr=[0]*n
    return merge1(arr,temparr,0,n-1)
def merge1(arr,temparr,left,right):
    invcount=0
    if right>left:
        mid=left+(right-left)//2
        invcount+=merge1(arr, temparr, left, mid)
        invcount+=merge1(arr, temparr, mid+1, right)
        invcount+=merge2(arr, temparr, left, mid,right)
    return invcount
def merge2(arr,temparr,left,mid,right):
    i=left
    j=mid+1
    k=left
    invcount = 0
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            temparr[k]=arr[i]
            i+=1
            k+=1
        else:
            temparr[k]=arr[j]
            invcount+=mid-i+1
            j+=1
            k+=1
    while i<=mid:
        temparr[k]=arr[i]
        i+=1
        k+=1
    while j<=right:
        temparr[k]=arr[j]
        j+=1
        k+=1
    for p in range(left,right+1):
        arr[p]=temparr[p]
    return invcount
arr = [1, 20, 6, 4, 5]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are", result)