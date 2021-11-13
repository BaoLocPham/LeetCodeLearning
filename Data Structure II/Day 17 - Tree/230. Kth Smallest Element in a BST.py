# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Approach 1: Recursive inorder travelsal
    # Time O(n)
    # Space O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rs = self.inorder(root, [])
        return rs[k - 1]

    def inorder(self, root, arr):
        if root == None:
            return arr
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
        return arr
    # Approach 2: Iterative inorder travelsal
    # Time O(n)
    # Space O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack, rs = [], []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            rs.append(current.val)
            current = current.right
        return rs[k - 1]
    # Approach 3: Optimized iterative inorder travelsal
    # Time O(n)
    # Space O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right