# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Approach : BFS
        # Time O(n)
        # Space O(n) -> size of the queue
        rs = []
        queue = []
        if not root:
            return rs
        queue.append(root)
        while queue:
            queueLen = len(queue)
            rss = []
            for i in range(queueLen):
                node = queue.pop(0)
                rss.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rs.append(rss)
        return rs