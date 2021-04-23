#!/usr/bin/env python
# coding: utf-8

# In[31]:


def pivotIndex(nums):
    left_sum=0
    for i in range(0,len(nums)):
        pivot=i
        j=i+1
        right_sum=sum(nums[j:])
        left_sum=sum(nums[:i])
        if left_sum==right_sum:
            return pivot
    return -1


# In[32]:


pivotIndex([1,7,3,6,5,6])


# In[34]:


pivotIndex([2,1,-1])


# In[42]:


pivotIndex([1,2,3])


# In[41]:


def pivotIndex(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumL = 0
        sumR = sum(nums)
        for i in range(len(nums)):
            sumR -= nums[i]
            if sumL == sumR:
                return i
            sumL += nums[i]
        return -1


# In[ ]:




