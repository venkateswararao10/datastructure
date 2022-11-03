class bst:
    def __init__(self,data):
        self.key = data
        self.left=None
        self.right=None
    def insert(root,val):
        if root is None:
            root.key = val
            return
        if root.key==val:
            return
        if root.key<val:
            if root.right:
                root.right.insert(val)
            else:
                root.right=bst(val)
        else:
            if root.left:
                root.left.insert(val)
            else:
                root.left=bst(val)
    def search(self,data):
        if self.key==data:
            print(f"{data} is found")
            return
        if data<self.key:
            if self.left:
                self.left.search(data)
            else:
               print(f"{data} is not found") 
        else:
            if self.right:
                self.right.search(data)
            else:
                print(f"{data} is not found")
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key,end=" ")
        if self.right:
            self.right.inorder()
    def preorder(self):
        print(self.key,end=" ")
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()
    def postorder(self):
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()
        print(self.key,end=" ")
def minValueNode(node):
  curr = node
  while(curr.left is not None):
    curr = curr.left

  return curr

# Given a binary search tree and a data, this function
# delete the key and returns the new root
def deleteNode(root, data):
    # Base Case
    if root is None:
      return root
    # If the data to be deleted
    # is smaller than the root's
    # data then it lies in left subtree
    if (data < root.key):
      root.left = deleteNode(root.left, data)
 
    # If the data to be delete
    # is greater than the root's
    # data then it lies in right subtree
    elif (data > root.key):
      root.right = deleteNode(root.right, data)
 
    # If data is same as root's data, then this is the node
    # to be deleted
    # Case 1 and Case 2
    else:
        # Node with no child
        # Deleted Node : Leaf Node
        if root.left is None and root.right is None:
          return None
        # Node with only one child
        if root.left is None:
          return root.right
        elif root.right is None:
          return root.left
 
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        # Case 3
        min_value = minValueNode(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.key = min_value.key
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, min_value.key)
 
    return root
root=bst(20)
l=[12,34,2,4,6,34]
for i in l:
    root.insert(i)
root.search(4)
root.search(66)
root.search(34)
root.inorder()
print()
root.preorder()
print()
root.postorder()
deleteNode(root, 20)
deleteNode(root,2)
root.preorder()