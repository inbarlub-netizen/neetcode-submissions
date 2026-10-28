# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        while fast and fast.next :
            fast=fast.next.next
            slow=slow.next
        cur= slow.next
        slow.next= None
        prev=None
        while cur:
            next_node=cur.next
            cur.next=prev
            prev= cur
            cur=next_node
        cur1= head
        cur2= prev
        while cur1 and cur2 :
            next1= cur1.next
            cur1.next=cur2
            next2= cur2.next
            cur2.next= next1
            cur1=next1
            cur2= next2
        return 
        


        