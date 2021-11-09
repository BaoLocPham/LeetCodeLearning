# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Approach 1: using hashMap to store the preorder key:value_preorder val: index_preorder
        # for find the value of the root in constant time
        # Solution: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/
        # The idea is you can build the binary tree from preorder array for the root and subtree using inorder array
        # Time O(n)
        # Space O(n)
        inorder_index_map = {}
        for index, val in enumerate(inorder):
            inorder_index_map[val] = index
        preorder_index = 0
        left, right = 0, len(preorder) - 1

        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no element to construct the tree
            if left > right: return None

            # select the preorder_index elelement as the root and increment it
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)

            # increase the preorder index for build the next tree
            preorder_index += 1

            # build the next left and right subtree -> inorder goes root left right
            root.left = array_to_tree(left, inorder_index_map[root_val] - 1)
            root.right = array_to_tree(inorder_index_map[root_val] + 1, right)
            return root

        return array_to_tree(left, right)

