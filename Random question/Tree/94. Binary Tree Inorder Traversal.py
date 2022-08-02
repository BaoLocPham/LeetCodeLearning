# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive Approach
    # Time O(n)
    # Space O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rs = []
        def helper(node):
            if node:
                helper(node.left)
                rs.append(node.val)
                helper(node.right)
        helper(root)
        return rs
        
    # Iterative Approach
    # Time O(n)
    # Space O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rs = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            rs.append(curr.val)
            curr = curr.right
        return rs
