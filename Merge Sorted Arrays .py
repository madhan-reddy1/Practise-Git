#!/usr/bin/env python
# coding: utf-8

# In[6]:


def Mergesorted(num1,num2):
    out=[]
    len1=len(num1)
    len2=len(num2)
    i=0
    j=0
    while i<len1 and j<len2:
        if num1[i]<num2[j]:
            out.append(num1[i])
            i+=1
        else:
            out.append(num2[j])
            j+=1
    while i<len1:
        out.append(num1[i])
        i+=1
    while j<len2:
        out.append(num2[j])
        j+=1
    return out


# In[7]:


num1=[1,2,3,9]
num2=[5,6,7,8]
Mergesorted(num1,num2)


# In[9]:




