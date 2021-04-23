#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TreeNode:
    def __init__(self,key,val,leftchild=None,rightchild=None,parent=None):
        self.key=key
        self.val=val
        self.leftchild=leftchild
        self.rightchild=rightchild
        self.parent=parent
        
    def hasLeftChild(self):
        return self.leftchild
    
    def hasRightChild(self):
        return self.rightchild

    def isLeftChild(self):
        return self.parent and self.parent.leftchild == self

    def isRightChild(self):
        return self.parent and self.parent.rightchild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightchild or self.leftchild)

    def hasAnyChildren(self):
        return self.rightchild or self.leftchild

    def hasBothChildren(self):
        return self.rightchild and self.leftchild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftchild = lc
        self.rightchild = rc
        if self.hasLeftChild():
            self.leftchild.parent = self
        if self.hasRightChild():
            self.rightchild.parent = self
    
    def displaynode(self):
        if self.key is not None:
            print(self.key, ":", self.val)
            if self.leftchild is not None:
                self.leftchild.displaynode()
            if self.rightchild is not None:
                self.rightchild.displaynode()
    
    def inorder(self):
        if self.key is not None:
            if self.leftchild is not None:
                self.leftchild.inorder()
            print(self.key, ":", self.val)
            if self.rightchild is not None:
                self.rightchild.inorder()


# In[6]:


class BinaryTree(TreeNode):
    def __init__(self):
        self.root=None
        self.size=0
    
    def length(self):
        return self.size
    
    def put(self,key,value):
        if self.root!=None:
            self._put(key,value,self.root)
        else:
            self.root=TreeNode(key,value)
        self.size=self.size+1
        
        
    def _put(self,key,value,currentNode):
        
        if  key<currentNode.key :
            if currentNode.hasLeftChild():
                self._put(key,value,currentNode.leftchild)
            else:
                currentNode.leftchild=TreeNode(key,value,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,value,currentNode.rightchild)
            else:
                currentNode.rightchild=TreeNode(key,value,parent=currentNode)
                
    def display(self):
        if self.root is None:
            return None
        else:
            #currentNode = self.root
            self.root.displaynode()
    
    def traversal_inorder(self):
        if self.root is None:
            return None
        else:
            #currentNode = self.root
            self.root.inorder()
    
    
    def __setitem__(self,k,v):
        self.put(k,v)
    
    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.val
            else:
                return None
        else:
            return None
    def _get(self,key,currentNode):
        if currentNode.key == key:
            return currentNode
        elif key<currentNode.key:
            return self._get(key,currentNode.leftchild)
        elif key>currentNode.key:
            return self._get(key,currentNode.rightchild)
        else:
            return None
    def __getitem__(self,key):
        return self.get(key)
    
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
    
    def delete(self,key):
        if self.size>1:
            nodetoremove=self._get(key,self.root)
            if nodetoremove:
                self.remove(nodetoremove)
                self.size=self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size=self.size-1
        else:
            raise KeyError("ERROR, Key NOT IN THERE")
    
    def __delitem__(self,key):    
        self.delete(key)
    
    def findSuccessor(self):
        
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                
                if self.isLeftChild():
                    
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    
    def spliceOut(self):
        if self.isLeaf:
            if self.isLeftChild():
                
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                
                if self.isLeftChild():
                    
                    self.parent.leftChild = self.leftChild
                else:
                    
                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
        else:
                    
            if self.isLeftChild():
                        
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
    
    def remove(self,currentNode):
        if currentNode.isLeaf():#no left or right child
            if currentNode==currentNode.parent.leftchild:
                currentNode.parent.leftchild=None
            else:
                currentNode.parent.rightchild=None
        elif currentNode.hasBothChildren():
            succ=currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key=succ.key
            currentNode.val=succ.val
        else:#one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftchild.parent=currentNode.parent
                    currentNode.parent.leftchild=currentNode.leftchild
                elif currentNode.isRightChild():
                    currentNode.leftchild.parent=currentNode.parent
                    currentNoder.parent.rightchild=currentNode.leftchild
                else:
                     currentNode.replaceNodeData(currentNode.leftchild.key,
                                    currentNode.leftchild.val,
                                    currentNode.leftchild.leftchild,
                                    currentNode.leftchild.rightchild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightchild.parent = currentNode.parent
                    currentNode.parent.leftchild = currentNode.rightchild
                elif currentNode.isRightChild():
                    currentNode.rightchild.parent = currentNode.parent
                    currentNode.parent.rightchild = currentNode.rightchild
                else:
                    currentNode.replaceNodeData(currentNode.rightchild.key,
                                    currentNode.rightchild.val,
                                    currentNode.rightchild.leftchild,
                                    currentNode.rightchild.rightchild)
        


# In[ ]:





# In[7]:


Tree=BinaryTree()


# In[ ]:





# In[8]:


Tree.put(500,"King")


# In[9]:


Tree.put(100,"sai")

