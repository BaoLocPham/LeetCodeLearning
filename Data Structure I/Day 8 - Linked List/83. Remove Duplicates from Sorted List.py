# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1: Iteration
        # Time O(n)
        # Space O(1)
        if not head:
            return head
        curr = head
        while curr.next:
            if curr.val==curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head