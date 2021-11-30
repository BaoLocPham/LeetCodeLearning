class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Approach 1: DP
        # Time O(n)
        # Space O(1)
        maxEnd, maxSoFar = nums[0], nums[0]
        for i in range(1, len(nums)):
            maxEnd = maxEnd + nums[i]
            # if maxEnd < nums[i]:
            #     maxEnd = nums[i]
            # if maxSoFar < maxEnd:
            #     maxSoFar = maxEnd
            maxEnd = max(maxEnd, nums[i])
            maxSoFar = max(maxSoFar, maxEnd)
        return maxSoFar
