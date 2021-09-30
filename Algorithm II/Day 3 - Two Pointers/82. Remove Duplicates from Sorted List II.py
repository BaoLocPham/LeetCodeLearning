# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1: Two pointers
        # Time O(n)
        # Space O(1)
        dummy = ListNode(next=head)
        slow, fast = dummy, head
        while fast:
            if fast.next and fast.val==fast.next.val:
                while fast.next and fast.val==fast.next.val:
                    fast = fast.next
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next
        return dummy.next
