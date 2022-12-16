class treenode:
  def __init__(self,data):
    self.data=data
    self.right=None
    self.left=None
class avl:
  def insert(self,root,val):
    if root is None:
        return treenode(val)
    else:
         if root.data==val:
             return root
         elif root.data >val:
             root.left=self.insert(root.left,val)
         else:
             root.right=self.insert(root.right,val)
    return root
  def getminvalue(self,root):
      if root is None or root.left is None :
          return root
      return self.getminvalue(root.left)
  def deletenode(self,root,val):
      if root is None:
          return root
      if root.data>val:
          root.left=self.deletenode(root.left,val)
      elif val>root.data:
          root.right=self.deletenode(root.right,val)
      else:
          if root.left is None:
              temp=root.right
              root=None
              return temp
          elif root.right is None:
              temp=root.left
              root=None
              return temp
          temp=self.getminvalue(root.right)
          root.data=temp.data
          root.right=self.deletenode(root.right,temp.data)
      return root
  def search(self,root,val):
    
        if root.data==val:
            print(f"{val} is found")
            return
        if val<root.data:
            if root.left:
                self.search(root.left,val)
            else:
               print(f"{val} is not found") 
        else:
            if root.right:
                self.search(root.right,val)
            else:
                print(f"{val} is not found")
        
 
  def preorder(self,root):
      if root:
          print(root.data)
          self.preorder(root.left)
          self.preorder(root.right)
tree=avl()
r=None
r=tree.insert(r,30)
r=tree.insert(r,40)
r=tree.insert(r,25)
r=tree.insert(r,40)
r=tree.insert(r,25)
r=tree.insert(r,50)
r=tree.insert(r,15)
r=tree.insert(r,-45)
tree.search(r,30)
r=tree.insert(r,5)
tree.preorder(r)
r=tree.deletenode(r,30)
print("preorder:")
tree.preorder(r)
tree.search(r,30)
