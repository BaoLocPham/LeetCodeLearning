"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Approach 1: BFS
        # Time O(n)
        # Space O(n) -> size of the queue
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            dummy = Node()
            while size>0:
                node = queue.popleft()
                dummy.next = node
                dummy = dummy.next
                if dummy.left:
                    queue.append(dummy.left)
                if dummy.right:
                    queue.append(dummy.right)
                size-=1
        return root

        # Approach 2: Iteration 3 pointers
        # Time O(n)
        # Space O(1)
        if not root:
            return None
        head = root
        while head:
            dummy = Node()
            tmp = dummy
            while head:
                if head.left:
                    tmp.next = head.left
                    tmp = tmp.next
                if head.right:
                    tmp.next = head.right
                    tmp = tmp.next
                head = head.next
            head = dummy.next
        return root