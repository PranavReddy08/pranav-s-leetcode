# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=set()
        c=head
        while c:
            if c in s:
                return True
            else:
                s.add(c)
                
            c=c.next
        return False
            
        
        
