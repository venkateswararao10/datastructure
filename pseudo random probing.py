'''Random Probing
Suppose that the hash table has b buckets. 
In linear open addressing the buckets are examined in the order (f(k)+i) % b, 0 <= i < b, where k is the key of the element being searched for. 
In random probing a pseudo-random number generator is used to obtain a random sequence R(i), 1 <= i < b where R(1), R(2), ... R(b-1) is a permutation of [1, 2, ..., b-1]. 
The buckets are examined in the order f(k), (f(k)+R(i)) % b, 1 <= i < b.
'''
import random
def randlist(arr):
    l=[i for i in range(1,len(arr))]  #or # r= random.randint(1,len(arr)-1)
    r=random.choice(l)
    return r
def hash(stri,arr):
 sum=0
 for i in stri:
   v=ord(i)
   sum=sum+v
 return sum%len(arr)
def insert(stri,arr): 
    key=hash(stri,arr)
    for j in range(len(arr)):
           ind=(key+randlist(arr))%len(arr)
           if arr[ind]==-1:
             arr[ind]=stri
             return
def dele(stri,arr):
 for i in range(len(arr)):
    if arr[i]==stri:
        arr[i]=-1
        print("its deleted")
        return
 print("string not found")
def search(stri,arr):
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
insert(s,a)
insert(s1,a)
insert(s2,a)
insert(s3,a)
insert(s4,a)
insert('raghu',a)
print(a)
search(s4,a)
search("rag",a)
dele(s,a)
dele("djt",a)
print(a)
