class doublehashing:
    def __init__(self):
        self.size=0
        self.arr=[-1 for _ in range(10)]
    def hash1(self,key):
          return key%len(self.arr)
    def hash2(self,key):
        return (1+key%(len(self.arr)-2))
    def isfull(self):
       if self.size==len(self.arr):
        return True
    def insertion(self,key):
        if self.isfull():
            return
        ind=self.hash1(key)
        if self.arr[ind]==-1 or self.arr[ind]=="dummy":
            self.arr[ind]=key
            self.size+=1
            return
        i=1
        while(True):
             inde=(self.hash1(key)+i*self.hash2(key))%len(self.arr) 
             if self.arr[inde]==-1 or self.arr[inde]=="dummy":
                self.arr[inde]=key
                self.size+=1
                break
             i+=1
    def search(self,key):
        i1=self.hash1(key)
        i2=self.hash2(key)
        i=0
        while self.arr[(i1+i*i2)%len(self.arr)] != key:
           if self.arr[((self.hash1(key)+i*self.hash2(key))%len(self.arr))]==-1:
            print("element not found")
            return False
        i=i+1
        print("key is found")
        return True
    def deletion(self,key):
        i1=self.hash1(key)
        i2=self.hash2(key)
        i=0
        while (self.arr[(i1+i*i2)%len(self.arr)]!=-1):
         if self.arr[(i1+i*i2)%len(self.arr)] == key:
            self.arr[(i1+i*i2)%len(self.arr)]="dummy"
            self.size-=1
            break
         i+=1
        else:
          print("element not found")
    def display(self):
        print(self.arr)
dh=doublehashing()
dh.insertion(12)
dh.insertion(30)
dh.insertion(99)
dh.insertion(20)
dh.insertion(45)
dh.insertion(42)

dh.display()
dh.search(44)
dh.deletion(45)
dh.display()
dh.insertion(45)
dh.display()
