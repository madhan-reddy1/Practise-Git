#!/usr/bin/env python
# coding: utf-8

# Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
# 
# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
# 
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# 
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2
#  
# Input: numbers = [-1,0], target = -1
# Output: [1,2]

# In[1]:


def twoSum(numbers,target):
        start=0
        end=len(numbers)-1
        while(start<end):
            total=numbers[start]+numbers[end]
            if total<target:
                start+=1
            elif total>target:
                end-=1
            else:
                return [start+1,end+1]


# In[2]:


twoSum(numbers = [2,7,11,15], target = 9)

