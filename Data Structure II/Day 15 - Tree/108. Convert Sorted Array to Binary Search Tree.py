# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Approach 1:
        # Travels the nums array using two pointers to find the mid value
        # Time O(n)
        # Space O(1)
        if len(nums)==1:
            return TreeNode(val=nums[0])
        head = self.solve(0,len(nums)-1, nums)
        return head
    def solve(self, low, hight, nums):
        if low>hight:
            return None
        mid = (low+hight)//2
        node = TreeNode(val=nums[mid])
        node.right = self.solve(mid+1,hight, nums)
        node.left = self.solve(low, mid-1, nums)
        return node