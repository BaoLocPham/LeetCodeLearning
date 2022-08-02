# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time O(n)
    # Space O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rs = []
        
        if not root:
            return rs
        queue = []
        queue.append(root)
        while queue:
            len_ = len(queue)
            tmp = []
            for _ in range(len_):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rs.append(tmp)
        return rs