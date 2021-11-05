# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1: basic math
        # Time O(n)
        # Space O(1)
        dummy = ListNode()
        current = dummy
        carry = 0
        p = l1
        q = l2
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            p = p.next if p else None
            q = q.next if q else None
            summ = x + y + carry
            carry = summ//10
            current.next = ListNode(val= summ%10)
            current = current.next
        if carry:
            current.next = ListNode(val=carry)
        return dummy.next