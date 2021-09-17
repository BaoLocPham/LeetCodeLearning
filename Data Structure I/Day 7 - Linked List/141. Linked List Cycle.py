# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Approach 1: using hashMap or whatever to store visited node
        # Time O(n)
        # Space O(n)
        # visited = []
        # point = head
        # while point:
        #     if point in visited:
        #         return True
        #     visited.append(point)
        #     point = point.next
        # return False
        # Approach 2: Using two pointer fast and slow
        # Time O(n)
        # Space O(1)
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False 