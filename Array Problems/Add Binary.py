#!/usr/bin/env python
# coding: utf-8

# In[14]:


def addBinary(a,b):
    i=len(a)-1
    j=len(b)-1
    sum=0
    result=''
    carry=0
    while i>=0 or j>=0:
        sum=carry
        if i>=0:
            sum+=int(a[i])
        if j>=0:
            sum+=int(b[j])
        result=str(sum%2)+result
        carry=sum//2
        
        i-=1
        j-=1
    if carry:
        result='1'+result
    return result


# In[12]:


addBinary(a = "1010", b = "1011")


# In[13]:


addBinary(a = "11", b = "1")

