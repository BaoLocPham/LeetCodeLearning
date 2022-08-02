# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Approach Recursive
    # Time O(n)
    # Space O(N)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def recursive_tree(current):
            nonlocal ans
            # if reached the end of a branch, return False
            if not current:
                return False
            
            # Left recursion
            left = recursive_tree(current.left)
            
            # Right recursion
            right = recursive_tree(current.right)
            
            # if the current node is one of p or q
            mid = current == p or current == q
            
            # if any two of the three flag left, right, mid become True
            if left + right + mid >= 2:
                ans = current
            
            # return True if either of the three flags is true
            return mid or left or right
        recursive_tree(root)
        return ans