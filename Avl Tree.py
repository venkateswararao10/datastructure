class treenode:
  def __init__(self,data):
    self.data=data
    self.right=None
    self.left=None
    self.height=1 
class avl:
  def getheight(self,root):
      if root is None:
          return 0
      return root.height
  def getbalance(self,root):
       if root is None:
          return 0
       return self.getheight(root.left) - self.getheight(root.right)
  def rightrotation(self,y):
      x=y.left
      t2=x.right
      x.right=y
      y.left=t2
      x.height=1+max(self.getheight(x.left),self.getheight(x.left))
      y.height=1+max(self.getheight(y.left),self.getheight(y.left))
      return x
  def leftrotation(self,x):
      y=x.right
      t2=y.left
      y.left=x
      x.right=t2
      x.height=1+max(self.getheight(x.left),self.getheight(x.left))
      y.height=1+max(self.getheight(y.left),self.getheight(y.left))
      return y
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
    
    root.height=1+max(self.getheight(root.left),self.getheight(root.right))
    balancefactor=self.getbalance(root)
    #ll rotation
    if balancefactor>1 and val<root.left.data:
        return self.rightrotation(root)
    if balancefactor<-1 and val>root.right.data:
        return self.leftrotation(root)
    if balancefactor>1 and val>root.left.data:
        root.left=self.leftrotation(root.left)
        return self.rightrotation(root)
    if balancefactor<-1 and val<root.right.data:
        root.right=self.rightrotation(root.right)
        return self.leftrotation(root)
    return root
     
  def inorder(self,root):
      if root:
          self.inorder(root.left)
          print(root.data)
          self.inorder(root.right)
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
      if root is None:
          return root
      root.height=1+max(self.getheight(root.right),self.getheight(root.left))
      balfac=self.getbalance(root)
      if balfac>1 and  self.getbalance(root.left)>=0:
          return self.rightrotation(root)
      if balfac<-1 and self.getbalance(root.right)<=0:
         return self.leftrotation(root)
      if balfac>1 and self.getbalance(root.left)<0:
          root.left=self.leftrotation(root.left)
          return self.rightrotation(root)
      if balfac<-1 and self.getbalance(root.right)>0:
          root.right=self.rightrotation(root.right)
          return self.leftrotation(root)
      return root
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
r=tree.insert(r,5)
tree.preorder(r)
r=tree.deletenode(r,30)
tree.preorder(r)
