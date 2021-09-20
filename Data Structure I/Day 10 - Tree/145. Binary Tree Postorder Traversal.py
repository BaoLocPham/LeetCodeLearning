# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # This is a DFS problems
        # Time O(n)
        # Space O(n) -> size of the stack
        # The Rule: Left, Right, Root
        stack, rs = [], []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                rs.insert(0, current.val) # reverse the process of inorder
                current = current.right # reverse the process of inorder
            current = stack.pop()
            current = current.left
        return rs