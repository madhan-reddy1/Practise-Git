#!/usr/bin/env python
# coding: utf-8

# In[40]:


def longestCommonPrefix(strs):
        lcp=""
        if len(strs)==0:
            return lcp
        else:
            minlen=len(strs[0])
            for i in range(1,len(strs)):
                if minlen>len(strs[i]):
                    minlen=len(strs[i])
            i=0
            while i<minlen:
                pivot=strs[0][i]
                for j in range(1,len(strs)):
                    if strs[j][i]!=pivot:
                        return lcp   
                lcp=lcp+pivot
                i+=1
            return lcp


# In[41]:


longestCommonPrefix(strs =["flower","flow","flight"])


# In[38]:


strs =""


# In[39]:


len(strs)

