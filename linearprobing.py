
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
print(hash("bye"))
def insertlinearprobing(stri,arr):
    key=hash(stri)
    for j in range(len(arr)):
           ind=(key+j)%len(stri)
           if arr[ind]==-1:
             arr.insert(ind,stri)
             break
s="abcd"
s1="abcd"
s2="hlo"
s3="bye"
a=[-1 for i in range(50)]
insertlinearprobing(s,a)
insertlinearprobing(s1,a)
insertlinearprobing(s2,a)
insertlinearprobing(s3,a)
print(a)
    
