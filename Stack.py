#!/usr/bin/env python
# coding: utf-8

# In[15]:


class Stack(object):
    
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]
    
    def Push(self,item):
        self.items.append(item)
    
    def Pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[len(self.items)-1]


# In[16]:


S1=Stack()


# In[17]:


S1.isEmpty()


# In[18]:


S1.Push("a")


# In[19]:


S1.isEmpty()


# In[21]:


S1.peek()


# In[25]:


S1.size()


# In[ ]:




