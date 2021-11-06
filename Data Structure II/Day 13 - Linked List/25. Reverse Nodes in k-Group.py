# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Approach 1:
        # Time O(n)
        # Space O(1)
        dummy = ListNode(next=head)
        groupPrev = dummy
        while True:
            kth = self.getK(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
