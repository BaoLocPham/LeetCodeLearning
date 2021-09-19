# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # This is an recusion-backtracking type problem
        # Approach 1: Iteration :)))
        # Time O(n+m)
        # Space O(1) using dummy node and tail node
        # dummy = ListNode()
        # tail = dummy
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         tail.next = l1
        #         l1 = l1.next
        #     else:
        #         tail.next = l2
        #         l2 = l2.next
        #     tail = tail.next
        #
        # tail.next = l1 if l1 else l2
        # return dummy.next
        # Approach 2: Recursion
        # Time O()
        # Space O()
        if not l1 or not l2:
            return l1 or l2  # l1 if l1 else l2 :)
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2