# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        oh=head
        eh=head.next
        o=oh
        e=eh
        
        while e and e.next:
            o.next=e.next
            o=o.next
            e.next=o.next
            e=e.next
        o.next=eh
        return head


        
