# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Approach 1: Recursion
        # Time O(n)
        # Space O(?)
        # if not root:
        #     return None
        # root.right, root.left = root.left, root.right
        # self.invertTree(root.right)
        # self.invertTree(root.left)
        # return root
        # Approach 2: Iteration
        # Time O(n)
        # Space O(n) size of the stack
        if not root:
            return None
        stack = []
        stack.append(root)
        current = root
        while stack and current:
            current = stack.pop()
            current.right, current.left = current.left, current.right
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return root