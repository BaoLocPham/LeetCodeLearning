# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # This is a BFS problem
        # Approach 1: Recursion
        # Time O(logn) -> not travels all node
        # Space O(?)
        # if not root:
        #     return None
        # if val==root.val:
        #     return root
        # elif val<root.val:
        #     return self.searchBST(root.left, val)
        # else:
        #     return self.searchBST(root.right, val)
        # Approach 2: Iteration
        # Time O(logn)
        # Space O(n) size of the queue
        queue = []
        queue.append(root)
        current = root
        while current and queue:
            current = queue.pop(0)
            if current.val == val:
                return current
            elif val < current.val and current.left:
                queue.append(current.left)
            elif val > current.val and current.right:
                queue.append(current.right)
        return None