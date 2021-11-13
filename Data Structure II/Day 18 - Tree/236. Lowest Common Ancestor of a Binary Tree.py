# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Approach 1: using three flags
        # Time O(n)
        # Space O(n)
        ans = None

        def recursive_tree(current_node):
            nonlocal ans
            # if reached the end of a branch, return False.
            if not current_node:
                return False

            # Left recursion
            left = recursive_tree(current_node.left)

            # Right recursion
            right = recursive_tree(current_node.right)

            # if the current_node is one of p or q:
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True
            if mid + left + right >= 2:
                ans = current_node

            # Return True if either of the tree bool value is true
            return mid or left or right

        # Traverse of the tree
        recursive_tree(root)
        return ans