# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Approach 1: using a boolean variable
        # Same approach as 10.2 Binary Tree Level order traversal
        # Time O(n)
        # Space O(n)
        rs, queue = [], []
        if not root:
            return []
        queue.append(root)
        # from right to left
        zigzag = False
        while queue:
            n = len(queue)
            rss = []
            for i in range(n):
                node = queue.pop(0)
                if zigzag:  # append to the front
                    rss.insert(0, node.val)
                else:  # append to the back
                    rss.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # print(queue)
            rs.append(rss)
            zigzag = not zigzag
        return rs

