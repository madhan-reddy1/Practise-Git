# -*- coding: utf-8 -*-
"""MergeSort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VY9cXr-yNuAn-DYo83wBNDVb6jn3DapK
"""

def merge_sort(arr):
  if len(arr)<=1:
    return arr
  else:
    mid=len(arr)//2
    lefthalf=arr[:mid]
    righthalf=arr[mid:]
    
    merge_sort(lefthalf)
    merge_sort(righthalf)

    i=0
    j=0
    k=0

    while i<len(lefthalf) and j<len(righthalf):
      if lefthalf[i]<righthalf[j]:
        arr[k]=lefthalf[i]
        i=i+1
      else:
        arr[k]=righthalf[j]
        j=j+1
      k=k+1
    
    while i<len(lefthalf):
      arr[k]=lefthalf[i]
      i=i+1
      k=k+1
    while j<len(righthalf):
      arr[k]=righthalf[j]
      j=j+1
      k=k+1

arr=[30,2133,231,1245,192]
merge_sort(arr)
arr

