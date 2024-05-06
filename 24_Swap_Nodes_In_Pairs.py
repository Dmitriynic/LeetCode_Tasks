#24_Swap_Nodes_In_Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        while current and current.next:
            rest = current
            fast = current.next
            
            prev.next = fast
            rest.next = fast.next
            fast.next = rest
            prev = rest
            current = rest.next
        return dummy.next

#faster than 76.94%, memory less than 90.11%