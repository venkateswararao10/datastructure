class hashtable:
    def __init__(self):
        self.tablesize=10
        self.arr=[None for _ in range(self.tablesize)]
    def hash(self,key):
        sum=0
        for char in key:
            i=ord(char)
            sum+=i
        return sum%self.tablesize
    def addele(self,key,value):
        hkey=self.hash(key)
        self.arr[hkey]=value
    def getele(self,key):
        hkey=self.hash(key)
        if self.arr[hkey]==None:
            print("element is not present")
            return
        print(self.arr[hkey])
    def delelem(self,key):
        hkey=self.hash(key)
        if self.arr[hkey]==None:
            print("element is not present")
            return
        self.arr[hkey] = None
ha=hashtable()
ha.addele('march 8', 125)
ha.addele('hello',17)
ha.getele('bye')
print(ha.hash('bye'))



'''
The Load factor is a measure that decides when to increase the HashTable capacity to maintain the search and insert operation complexity of O(1). The default load factor of HashMap used in java, for instance, is 0.75f (75% of the map size)

rehashing means hashing again. Basically, when the load factor increases to more than its pre-defined value (default value of load factor is 0.75), the complexity increases.

Rehashing is a collision resolution technique. Rehashing is a technique in which the table is resized, i.e., the size of table is doubled by creating a new table. It is preferable is the total size of table is a prime number. There are situations in which the rehashing is required. • When table is completely full.
'''