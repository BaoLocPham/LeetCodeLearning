# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(node, prev=None) -> Optional[ListNode]:
        # This function is a helper function for recurive approach
        if not node:
            return prev
        nxt = node.next
        node.next = prev
        return self.reverse(nxt, node)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1: Iterative
        # Time O(n)
        # Space O(1)
        # if not head:
        #     return head
        # curr = head
        # prev = None
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev
        # Approach 2: Recurion
        # Time O(n)
        # Space O(1)
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            return self.reverse(head, None)