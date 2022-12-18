def minheapify(arr, n, i):
	smallest = i # Initialize smallest as root
	l = 2 * i + 1 # left = 2*i + 1
	r = 2 * i + 2 # right = 2*i + 2

# See if left child of root exists and is
# smaller than root

	if l < n and arr[l] < arr[i]: # arr[i] is same as arr[smallest]
		smallest = l

# See if right child of root exists and is
# smaller than root

	if r < n and arr[r] < arr[smallest]:
		smallest = r

# Change root, if needed

	if smallest != i:
		(arr[i], arr[smallest]) = (arr[smallest], arr[i]) # swap

# Heapify the root.

		minheapify(arr, n, smallest)

def insert(arr,ele):
    size=len(arr)
    if size==0:
        arr.append(ele)
    else:
        arr.append(ele)
        for i in range(len(arr)// 2 - 1, -1, -1):
		        minheapify(arr, len(arr), i)

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
		        minheapify(arr, n, i)
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
        minheapify(arr, len(arr), i)


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
