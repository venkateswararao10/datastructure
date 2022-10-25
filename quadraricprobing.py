
def hash(stri):
 sum=0
 for i in stri:
   v=ord(i)
   if  (v>=65 and v<=90):
      hashval=v-64
   elif (v>=97 and v<=122):
       hashval=v-96
   sum=sum+hashval
 return sum
print(hash("cd"))
def insertquadraticprobing(stri,arr):
    key=hash(stri)
    if arr[key%len(arr)]==-1:
        arr[key%len(arr)]=stri
        return
    for j in range(len(arr)):
           ind=(key+j*j)%len(arr)
           if arr[ind]==-1:
             arr[ind]=stri
             return
def delquadraticprobing(stri,arr):
 for i in range(len(arr)):
    if arr[i]==stri:
        arr[i]=-1
        print("its deleted")
        return
 print("string not found")
def searchquadraticprobing(stri,arr):
    for i in range(len(arr)):
     if arr[i]==stri:
        print(f"{stri} is found")
        return
    print(f"{stri} is not found")
s1="cd"
s2="cd"
s="hlo"
s3="bye"
s4="xy"
a=[-1 for i in range(10)]
insertquadraticprobing(s,a)
insertquadraticprobing(s1,a)
insertquadraticprobing(s2,a)
insertquadraticprobing(s3,a)
insertquadraticprobing(s4,a)
print(a)
searchquadraticprobing(s4,a)
searchquadraticprobing("rag",a)
delquadraticprobing("cd",a)
delquadraticprobing("djt",a)
print(a)
    
