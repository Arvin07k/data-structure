# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a=head
        b=head
        while n>0 and b:
            b=b.next
            n-=1
        
        while b and b.next:
            a=a.next
            b=b.next
        if a == head and not b:
            return head.next

        a.next =a.next.next

        return head
        

        
            

        