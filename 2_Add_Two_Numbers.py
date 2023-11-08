#2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        decimal = 0
        while l1 or l2 or decimal:
            if l1:
                l1Val = l1.val
            else:
                l1Val = 0
            if l2:
                l2Val = l2.val
            else:
                l2Val = 0
            curr_val = curr.val + l1Val + l2Val
            curr.val = curr_val % 10
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
            decimal = curr_val // 10
            if l1 or l2 or decimal:
                curr.next = ListNode(decimal)
                curr = curr.next
        return head
    
#beat 59% by speed and 46% by memory