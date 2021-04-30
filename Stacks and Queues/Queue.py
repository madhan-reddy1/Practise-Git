#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Queue(object):
    
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[len(self.items)-1]


# In[4]:


S1=Queue()


# In[5]:


S1.isEmpty()


# In[8]:


S1.enqueue("a")


# In[9]:


S1.isEmpty()


# In[10]:


S1.peek()


# In[12]:


S1.dequeue()

