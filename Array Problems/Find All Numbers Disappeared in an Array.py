#!/usr/bin/env python
# coding: utf-8

# In[1]:


def findDisappearedNumbers(nums):
    out=[]
    for i in range(0,len(nums)):
        if i+1 in nums:
            continue
        else:
            out.append(i+1)
    return out


# In[18]:


findDisappearedNumbers([1,3,4,3])


# In[17]:


def findDisappearedNumbers(nums):
    l1=set(range(1,len(nums)+1))
    nums=set(nums)
    return l1.difference(nums)


# In[14]:


nums=[1,3,4,3]
l1=range(1,len(nums)+1)
print(l1)

