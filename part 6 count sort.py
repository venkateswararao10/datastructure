def countsort(arr):
    print(arr)
    maxi=max(tuple(arr))
    freq=[0 for i in range(maxi+1)] 
    for i in range(len(arr)):
        freq[arr[i]]+=1
    print(freq)
    for i in range(1,maxi+1):
        freq[i] += freq[i-1]
    print(freq)
    outarr=[0 for i in range(len(arr))]
    for i in range(len(arr)-1,-1,-1):
        outarr[freq[arr[i]]-1]=arr[i]
        freq[arr[i]]-=1
    return(outarr)
      


arr=eval(input("enter a list"))

result=countsort(arr)
print(result)