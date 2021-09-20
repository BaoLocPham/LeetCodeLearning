# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # This is a DFS problems
        # Time O(n)
        # Space O(n) -> size of the stack
        # The Rule is: Root, Left, Right
        rs = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                rs.append(current.val)
                current = current.left
            current = stack.pop()
            current = current.right
        return rs