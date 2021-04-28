#!/usr/bin/env python
# coding: utf-8

# In[45]:


def strStr(haystack, needle):
    if needle=="" and haystack=="":
        return 0
    else :
        index=haystack.find(needle);
        return index


# In[53]:


strStr(haystack = "hello", needle = "ll")


# In[54]:


strStr(haystack = "aaaaa", needle = "bba")


# In[67]:


strStr("abc","c")


# In[66]:


def strStr(haystack,needle):
    len1=len(haystack)
    len2=len(needle)
    if len1<len2:
        return -1
    else:
        for i in range(0,len1-len2+1):
            print(i)
            for j in range(0,len2):
                if haystack[i+j]!=needle[j]:
                    break
            if j+1==len2:
                return i
        return -1


# In[ ]:





# In[ ]:




