class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Approach 1: Sliding windows:
        # Time O(n)
        # Space O(1)
        if k<=1:
            return 0
        prod = 1
        count = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod>=k:
                prod /= nums[left]
                left+=1
            count += right-left+1
        return count