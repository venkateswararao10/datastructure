def sort_without_sorting(arr):
    zerocount=0
    onecount=0
    #time complexity=o(n)
    #space complexity=o(1) here space complexity is extra space is taken if not taken space like taking another datastructurelike list,dictionary etc.. and variable  are not consider in space complexity then o(1) is space complexity
    for i in range(len(arr)):
        if arr[i]==0:
            zerocount+=1
        if arr[i]==1:
            onecount+=1
    for i in range(zerocount):
        arr[i]=0
    for i in range(zerocount,zerocount+onecount):
        arr[i]=1
    for i in range(zerocount+onecount,len(arr)):
        arr[i]=2
    return arr
arr=[0, 1, 2, 1, 0, 2, 1, 2] 
result=sort_without_sorting(arr)
print(result)