# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # OG idea by StefanPochmann https://leetcode.com/problems/binary-tree-right-side-view/discuss/56064/5-9-Lines-Python-48%2B-ms
        # Approach 1: Recursive, combine right and left
        # Time O(n^2)
        # Space O(1)

        #  1
        # / \
        # 2  3  we'll skip the node that blocked by the right neighbour
        # /
        # 4
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val]+right+left[len(right):]

        # Approach 2: Recursive, first come first serve
        # Time O(n)
        # Space O(1)
        def collect(node, depth):
            if node:
                if depth == len(view): # add value whenever it reach a new record
                    view.append(node.val)
                collect(node.right, depth + 1)
                collect(node.left, depth + 1)

        view = []
        collect(root, 0)
        return view

        # Approach 3: Iterative, level by level
        # Time O(n)
        # Space O(1)
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val,
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view