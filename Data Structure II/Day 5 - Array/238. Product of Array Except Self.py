class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Approach 1: Implementation
        # Time O(n) -> travel right and then travel left
        # Space O(1) -> if we not count the res array
        n = len(nums)
        res = [1]*n
        # we go left
        left=1
        for i in range(n):
            if i>0:
                left = left * nums[i-1]
            res[i] = left
        # then go right
        right = 1
        for i in range(n-1, -1, -1):
            if i<n-1:
                right = right*nums[i+1]
            res[i] *= right
        return res