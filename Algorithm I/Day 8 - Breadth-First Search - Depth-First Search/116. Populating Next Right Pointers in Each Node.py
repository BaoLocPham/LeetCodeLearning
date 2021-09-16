"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # This problem is DFS
        # Approach 1: pointer points to the parent node and set next on children node
        # Time O(logn)
        # Space O(1) not using extra memory
        if root == None:
            return None
        leftNode = root
        while leftNode.left != None:
            head = leftNode
            while head:
                head.left.next = head.right
                if head.next != None:
                    head.right.next = head.next.left
                head = head.next
            leftNode = leftNode.left
        return root