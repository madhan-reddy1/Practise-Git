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