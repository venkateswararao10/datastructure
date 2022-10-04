def countsort(l,place):
    freq=[0 for i in range(10)]
    output = [0 for i in range(len(l))]
    for i in range(len(l)):
        indexele=l[i]//place
        freq[indexele%10]+=1
    for i in range(1,10):
        freq[i]+=freq[i-1]
    for i in range(len(l)-1,-1,-1):
         indexele=l[i]//place
         output[freq[indexele%10]-1]=l[i]
         freq[indexele%10]-=1
    for i in range(len(l)):
        l[i]=output[i]
def radixsort(l):
    maxele=max(l)
    digitplace=1
    while maxele//digitplace>0:
        countsort(l,digitplace)
        digitplace*=10

arr=eval(input("enter a list"))
radixsort(arr)
print(arr)