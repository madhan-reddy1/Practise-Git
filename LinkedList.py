#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


# In[25]:


class LinkedList:
    def __init__(self):
        self.head=None
    
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head =new_node
        
    def insert_After(self,node,data):
        new_node=Node(data)
        if node is None:
            print("no input provided")
        i=self.head
        while i.next is not None:
            if i.next.data==node:
                break
            i=i.next
        if i.next is None:
            print("Not in the list")
        else:
            new_node=Node(data)
            new_node.next=i.next
            i.next=new_node
            

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None: 
            self.head = new_node
            return 
        last = self.head 
        while (last.next): 
               last = last.next
        last.next=new_node
    
    def printList(self): 
        current = self.head
        if self.head==None:
            print("No data")
        while current!=None:
            print(current.data),
            current = current.next


# In[26]:


A=LinkedList()


# In[27]:


A.insert_at_end(56)
A.insert_at_end(85)


# In[30]:


A.printList()


# In[29]:


A.insert_After(85,89)

