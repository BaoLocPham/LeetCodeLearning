# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Approach: Two pointers
        # Time O(n)
        # Space O(1)
        left_head, right_head = ListNode(), ListNode()
        left_tail, right_tail = left_head, right_head
        
        while head:
            if head.val < x:
                left_tail.next = head
                left_tail = left_tail.next
            else:
                right_tail.next = head
                right_tail = right_tail.next
            head = head.next
        left_tail.next = right_head.next
        right_tail.next = None
        return left_head.next
            