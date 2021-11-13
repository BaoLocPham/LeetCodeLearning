# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorderArray = self.inorder(root)
        self.currentIndex = 0
        print(self.inorderArray)

    def inorder(self, root):
        stack, rs = [], []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            rs.append(current.val)
            current = current.right
        return rs

    def next(self) -> int:
        ss = self.inorderArray[self.currentIndex]
        self.currentIndex += 1
        return ss

    def hasNext(self) -> bool:
        return self.currentIndex != len(self.inorderArray)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()