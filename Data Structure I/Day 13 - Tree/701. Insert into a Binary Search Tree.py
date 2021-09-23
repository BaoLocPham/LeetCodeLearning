# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Approach 1: Recurion
        # Time O(logn)
        # Space O(?)
        # if not root:
        #     return TreeNode(val=val)
        # if val<root.val:
        #     if not root.left:
        #         root.left = TreeNode(val)
        #     else:
        #         self.insertIntoBST(root.left, val)
        # if val>root.val:
        #     if not root.right:
        #         root.right = TreeNode(val)
        #     else:
        #         self.insertIntoBST(root.right, val)
        # return root

        # Approach 2: Iteration
        # Time O(logn)
        # Space O(logn) -> size of the stack or queue or whatever you want to store
        current = root
        stack = []
        stack.append(current)
        if not current:
            return TreeNode(val=val)
        while current and stack:
            current = stack.pop(0)
            if val < current.val:
                if current.left:
                    stack.append(current.left)
                else:
                    current.left = TreeNode(val=val)
                    return root
            elif val > current.val:
                if current.right:
                    stack.append(current.right)
                else:
                    current.right = TreeNode(val=val)
                    return root