# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Approach 1: Recursion
    # Time O(n)
    # Space O(?)
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     return self.isValid(root, -10**11, 10**10)
    # def isValid(self, root, minVal, maxVal):
    #     if not root:
    #         return True
    #     if root.val>=maxVal or root<=minVal:
    #         return False
    #     return self.isValid(root.left, minVal, root.val) and self.isValid(root.right, root.val, maxVal)
    
    # Approach 2: Iteration
    # Time O(n)
    # Space O(n) -> size of stack
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if (prev and prev.val >= root.val):
                return False
            prev = root
            root = root.right
        return True