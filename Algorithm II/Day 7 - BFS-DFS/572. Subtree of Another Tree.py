# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Approach 1: Recursion DFS
        # Time O(n)
        # Space O(?)
        def compare(root, subroot):
            if not root and not subroot:
                return True
            elif not root or not subroot:
                return False
            else:
                return root.val == subroot.val and compare(root.left, subroot.left) and compare(root.right,
                                                                                                subroot.right)

        if not root: return False
        return compare(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)