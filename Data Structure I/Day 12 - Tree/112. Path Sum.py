# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Approach 1: Recursion
        # Time O(n)
        # Space O(?)
        # def hasSum(node, sumVal):
        #     if node and not node.left and not node.right:
        #         if sumVal+node.val==targetSum:
        #             return True
        #         return False
        #     if node:
        #         return hasSum(node.left, sumVal+node.val) or hasSum(node.right, sumVal+node.val)
        # return hasSum(root, 0)
        # Approach 2: Iteration
        # Time O(n)
        # Space O(n) -> size of two stack
        if not root:
            return False
        sum_stack = []
        node_stack = []
        sum_stack.append(root.val)
        node_stack.append(root)
        current = root
        while current and node_stack:
            current = node_stack.pop()
            curr_sum = sum_stack.pop()
            if not current.right and not current.left and curr_sum == targetSum:
                return True
            if current.left:
                node_stack.append(current.left)
                sum_stack.append(curr_sum + current.left.val)
            if current.right:
                node_stack.append(current.right)
                sum_stack.append(curr_sum + current.right.val)
        return False