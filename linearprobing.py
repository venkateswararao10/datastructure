
def hash(stri,arr):
 sum=0
 for i in stri:
   v=ord(i)
   sum=sum+v
 return sum%len(arr)
def insertlinearprobing(stri,arr):
    key=hash(stri,arr)
    for j in range(len(arr)):
           ind=(key+j)%len(arr)
           if arr[ind]==-1:
             arr[ind]=stri
             return
def dellinearprobing(stri,arr):
 for i in range(len(arr)):
    if arr[i]==stri:
        arr[i]=-1
        print("its deleted")
        return
 print("string not found")
def searchlinearprobing(stri,arr):
    for i in range(len(arr)):
     if arr[i]==stri:
        print(f"{stri} is found")
        return
    print(f"{stri} is not found")
s="abcd"
s1="abcd"
s2="hlo"
s3="bye"
s4="xy"
a=[-1 for i in range(10)]
insertlinearprobing(s,a)
insertlinearprobing(s1,a)
insertlinearprobing(s2,a)
insertlinearprobing(s3,a)
insertlinearprobing(s4,a)
print(a)
searchlinearprobing(s4,a)
searchlinearprobing("rag",a)
dellinearprobing(s4,a)
dellinearprobing("djt",a)
print(a)
    
