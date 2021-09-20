# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # This is a DFS problems
        # Time O(n)
        # Space O(n) -> size of the stack
        # The Rule: Left, Root, Right
        stack = []
        rs = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            rs.append(current.val)
            current = current.right
        return rs



