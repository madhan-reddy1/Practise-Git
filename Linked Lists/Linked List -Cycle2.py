# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if (head== None or head.next== None):
            return None
        i=head
        j=head
        while j and j.next:    
            i=i.next
            j=j.next.next
            if i==j:
                i=head
                while i!=j:
                    i=i.next
                    j=j.next
                return i
        return None