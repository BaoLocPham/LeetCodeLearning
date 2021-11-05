# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Approach 1: swap head when one pointer reach the end
        # Time O(n)
        # Space O(1)
        p = headA
        q = headB
        while p is not q:
            p = p.next if p else headB
            q = q.next if q else headA

        return p
    # the idea is if you switch head, the possible difference between length would be countered.
    # On the second traversal, they either hit or miss.
    # if they meet, pa or pb would be the node we are looking for,
    # if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None