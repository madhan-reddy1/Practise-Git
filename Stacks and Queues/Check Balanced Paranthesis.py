#!/usr/bin/env python
# coding: utf-8

# In[7]:


from Stack import Stack


# In[12]:


def ChecK_Balance_Paranthesis(s):
    
    if len(s)%2!=0:
        return False
    
    opening=set("({[")
    
    matching=set([("(",")" ),("[","]" ),("{","}" )])
    
    check=Stack()
    isbalanced=True
    index=0
    length=len(s)
    while index<length and isbalanced:
        paren=s[index]
        
        if paren in opening :
            check.Push(paren)
        else :
            
            if length==0:
                isbalanced=False
            else:
                last_index=check.Pop()
            
            if (last_index,paren) not in matching:
                isbalanced=False
        index+=1
    if check.isEmpty and isbalanced:
        return True
    else:
        return False


# In[19]:


from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print('ALL TEST CASES PASSED')
        
# Run Tests

t = TestBalanceCheck()
t.test(ChecK_Balance_Paranthesis)

