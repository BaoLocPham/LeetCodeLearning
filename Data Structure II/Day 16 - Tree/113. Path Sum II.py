# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Approach: is similar to the 112. Path Sum problem
        #  using stack
        # Time O(n)
        # Space O(n)
        if not root:
            return []
        stack = [(root, targetSum - root.val, [root.val])]
        rs = []
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                rs.append(ls)
            if curr.right:
                stack.append((curr.right, val - curr.right.val, ls + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, val - curr.left.val, ls + [curr.left.val]))

        return rs