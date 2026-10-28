# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        cur1= list1
        cur2= list2
        start= ListNode(0)
        cur_res=start
        while(cur1 is not None and cur2 is not None):
            if cur1.val<=cur2.val:
                cur_res.next=cur1
                cur1=cur1.next
            else:
                cur_res.next=cur2
                cur2=cur2.next
            cur_res=cur_res.next
        if cur1 is not None:
            cur_res.next=cur1
        if cur2 is not None:
            cur_res.next=cur2
        return start.next



        