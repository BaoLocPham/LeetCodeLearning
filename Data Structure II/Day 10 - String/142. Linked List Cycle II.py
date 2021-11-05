# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Approach 1: Well, i read this solution in the dicussion :)
        # Time O(n?)
        # Space O(1)
        if not head or not head.next:
            return None
        slow, fast, entry = head, head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast==slow: # there is cycle
                # when fast and slow encounter 
                # find the entry of the cycle by moving entry and slow forward
                # when entry and slow encounter -> this is the entry of the cycle
                while slow!=entry: # 
                    slow = slow.next
                    entry = entry.next
                return entry
        return None