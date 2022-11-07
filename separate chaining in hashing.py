class separatechaining:
    def __init__(self):
        self.size=10
        self.arr=[[] for i in range(self.size)]
    def hash(self,key):
        sum=0
        for i in key:
           v=ord(i)
           sum=sum+v
        return sum%self.size
    def addele(self,key):
        hk=self.hash(key)
        self.arr[hk].append(key)
    def delele(self,key):
        for i in range(len(self.arr)):
            for j in self.arr[i]:
                if key==j:
                    print("element deleted")
                    self.arr[i].remove(key)
                    return
        print("element not found")
    def printele(self):
           for i in range(len(self.arr)):
            print(i,end=" ")
            for j in self.arr[i]:
                print("-->",end=" ")
                print(j,end=" ")
            print()
ha=separatechaining()
ha.addele("hlo sir")
ha.addele("bye")
ha.addele("dj tillu") 
ha.printele()       
ha.delele("yrt")
ha.delele("hlo sir")
ha.printele()
print(ha.hash('bye'))