#!/usr/bin/env python
# coding: utf-8

# In[5]:


def thirdMax(nums):
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            if nums[0]>nums[1]:
                return nums[1]
            else:
                return nums[0]
        else:
            max1=None
            second_max=None
            third_max=null
            for num in nums:
                if num==max1 or num==second_max or num ==third_max:
                    continue
        
                if max1==None or num>max1:
                    third_max=second_max
                    second_max=max1
                    max1=num
                elif second_max==None or num>second_max:
                    third_max=second_max
                    second_max=num
                elif thirdmax==None or num>third_max:
                    third_max=num
            if third_max==None:
                return max1


# In[ ]:




