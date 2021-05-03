#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


# In[ ]:





# In[5]:


def cycle_check(node):
    i=node
    j=node
    while j and j.nextnode!=None:
        i=i.nextnode
        j=j.nextnode.nextnode
        if i==j:
            return True
        index+=1
    return False        


# In[7]:


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
cycle_check(a)


# In[ ]:




