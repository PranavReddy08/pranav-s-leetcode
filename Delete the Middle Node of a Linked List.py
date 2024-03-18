# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=head
        f=head
        if head.next==None:
            return None

        while f and f.next:
            f=f.next.next
            prev=s
            s=s.next
        prev.next=s.next
        return head
        
