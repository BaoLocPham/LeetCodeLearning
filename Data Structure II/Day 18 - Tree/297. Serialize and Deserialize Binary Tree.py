# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []

        def build_string(node):
            nonlocal vals
            if node:
                vals.append(str(node.val))
                build_string(node.left)
                build_string(node.right)
            else:
                vals.append("X")

        build_string(root)
        return ",".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = data.split(",")[:-1]

        def build_tree(queue):
            if len(queue) == 0:
                return None
            val = queue.pop(0)
            if val == "X" or val == "":
                return None
            else:
                node = TreeNode(val=int(val))
                node.left = build_tree(queue)
                node.right = build_tree(queue)
                return node

        root = build_tree(queue)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))