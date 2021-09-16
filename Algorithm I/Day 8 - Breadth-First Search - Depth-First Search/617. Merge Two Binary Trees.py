# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # This a DFS problem

        # Approach 1: Recursion
        # Time O(m) n is the minimum nodes to travel
        # Space O(m)
        # if (root1==None):
        #     return root2
        # if (root2==None):
        #     return root1
        # curNode = TreeNode(val=root1.val+root2.val)
        # curNode.left = self.mergeTrees(root1.left, root2.left)
        # curNode.right = self.mergeTrees(root1.right, root2.right)
        # return curNode
        # Approach 2: Iteration
        if root1 == None:
            return root2
        stack = []
        stack.append(TreeNode(left=root1, right=root2))
        while stack:
            node = stack.pop()
            if node.left == None or node.right == None:
                continue
            node.left.val += node.right.val if node.right else 0
            if node.left.left == None:
                node.left.left = node.right.left
            else:
                stack.append(TreeNode(left=node.left.left, right=node.right.left))
            if node.left.right == None:
                node.left.right = node.right.right
            else:
                stack.append(TreeNode(left=node.left.right, right=node.right.right))
        return root1