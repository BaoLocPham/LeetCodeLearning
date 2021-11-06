# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1:
        # Time O(n)
        # Space O(1)
        dummy = ListNode(next=head)
        prev = dummy
        # prev -> a -> b -> b.next
        # prev -> b -> a -> b.next
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            prev.next, a.next, b.next = b, b.next, a
            prev = a
        return dummy.next