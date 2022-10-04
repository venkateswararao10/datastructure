def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                  min_index=j        
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[70,50,10,80,65,90]
result=selectionsort(arr)
print(arr)
# time complexity=o(n^2)
# space complexity=o(1)