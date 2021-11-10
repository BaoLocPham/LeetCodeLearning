# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Recursively find the node that has the same value as the key, while setting the left/right nodes equal to the returned subtree
        # Once the node is found, have to handle the below 4 cases
        # - node doesn't have left or right - return null
        # - node only has left subtree- return the left subtree
        # - node only has right subtree- return the right subtree
        # - node has both left and right - find the minimum value in the right subtree,
        # set that value to the currently found node, then recursively delete the minimum value in the right subtree
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            min_right = self.findMin(root.right)
            root.val = min_right.val
            root.right = self.deleteNode(root.right, root.val)
        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node
