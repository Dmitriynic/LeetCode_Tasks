# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            head.val = ''
            return head
        l = head
        r = head.next
        for i in range(n - 1):
            r = r.next
        if r:
            while r.next:
                l = l.next
                r = r.next
            if l.next.next:
                l.next = l.next.next
            else:
                l.next = None
        else:
            head = head.next
        return head
#time 42ms faster than 46.41%, memory 16.2mb, less than 37.67%.
#complexity O(N)