class node:
    def __init__(self,data):
        self.next =None
        self.data = data
class linkedlist:
    def __init__(self):
        self.head=None
    def insertatbeginning(self, newdata):
        newnode=node(newdata)
        if self.head is None:
         self.head=newnode
         return
        newnode.next=self.head
        self.head=newnode
    def insertatend(self,newdata):
        newnode=node(newdata)
        if self.head is None:
         self.head=newnode
         return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=newnode
    def length(self):
        temp=self.head
        lengt=0
        while(temp):
            temp=temp.next
            lengt=lengt+1
        return lengt
    def atanypositioninsertion(self,newdata,pos):
        if pos<0:
            print("out of range")
            return
        if (pos>self.length()): 
            print("out of range")
            return
        newnode=node(newdata)
        if self.head is None:
         self.head=newnode
         return
        temp=self.head
        if(pos==0):
            newnode.next=self.head
            self.head=newnode
            return
        i=0
        while(i<pos-1):
            temp=temp.next
            i=i+1
        newnode.next=temp.next
        temp.next=newnode        
    def delatanypos(self,pos):
        if pos<0:
            print("out of range")
            return
        if (pos>=self.length()): 
            print("out of range")
            return
        if self.head is None:
         print("list empty")
         return
        temp=self.head
        if(pos==0):
            self.head=temp.next
            temp=None
            return
        for i in range(pos-1):
            temp=temp.next
        nextptr=temp.next.next
        temp.next=None
        temp.next=nextptr
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def searchdata(self,key):
        temp=self.head
        while(temp):
            if(temp.data==key):
                return True
            temp=temp.next
        return False
ll=linkedlist()
ll.atanypositioninsertion(123,9)
ll.insertatbeginning(5)
ll.insertatbeginning(2)
ll.insertatend(77)
ll.atanypositioninsertion(345,0)
ll.atanypositioninsertion(789,4)
ll.insertatbeginning(6)
ll.insertatend(88)
ll.atanypositioninsertion(987,1)
print(" len= ",ll.length())
ll.display()
print("after deletion")
ll.delatanypos(0) # delete at beginning position here at deletion we given index
ll.display()
print(" len= ",ll.length())
ll.delatanypos(6)# delete at end of list
ll.display()
print(" len= ",ll.length())
ll.delatanypos(3)# delete at 3rd index
ll.display()
print(" len= ",ll.length())
ll.delatanypos(9)# delete at 9th index
ll.display()
print(ll.searchdata(88))
print(ll.searchdata(987))
print(ll.searchdata(789))
print(ll.searchdata(2))
key = 13
if ll.searchdata(key):
    print(str(key) + " is found")
else:
    print(str(key) + " is not found")

