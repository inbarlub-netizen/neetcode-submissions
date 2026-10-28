# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        space = head
        cur= head
        for i in range(n):
            space= space.next
        if space is None:
            return head.next
        before= cur
        while space:
            before= cur
            cur=cur.next
            space= space.next
        before.next= cur.next
        return head
        
        
        