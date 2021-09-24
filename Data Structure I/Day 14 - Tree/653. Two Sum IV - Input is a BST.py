# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Approach 1: Iteration
        # Time O(n)
        # Space O(n)
        if not root:
            return False
        visited = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                if (k - root.val) in visited:
                    return True
                visited.append(root.val)
                root = root.left
            root = stack.pop()
            root = root.right
        return False
