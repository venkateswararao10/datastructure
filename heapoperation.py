def maxheapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1 # left = 2*i + 1
	r = 2 * i + 2 # right = 2*i + 2

# See if left child of root exists and is
# greater than root

	if l < n and arr[i] < arr[l]:
		largest = l

# See if right child of root exists and is
# greater than root

	if r < n and arr[largest] < arr[r]:
		largest = r

# Change root, if needed

	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i]) # swap

# Heapify the root.

		maxheapify(arr, n, largest)

def insert(arr,ele):
    size=len(arr)
    if size==0:
        arr.append(ele)
    else:
        arr.append(ele)
        for i in range(len(arr)// 2 - 1, -1, -1):
		        maxheapify(arr, len(arr), i)

def delete():
    size=len(arr)
    if size==0:
        print("no element is present in array")
        return
    else:
        arr[0],arr[size-1]=arr[size-1],arr[0]
        a=arr.pop()
        n=len(arr)
        for i in range(n // 2 - 1, -1, -1):
		        maxheapify(arr, n, i)
    return a
def deleteele(ele):
    size=len(arr)
    if size==0:
        print("no element is present in array")
        return
    i=0
    for i in range(0,size):
        if ele==arr[i]:
            break
    arr[i],arr[size-1]=arr[size-1],arr[i]
    arr.remove(ele)#arr.pop()
    for i in range((len(arr)//2)-1, -1, -1):
        maxheapify(arr, len(arr), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)
print(arr)
print(delete())
print(arr)
deleteele(4)
print(arr)
