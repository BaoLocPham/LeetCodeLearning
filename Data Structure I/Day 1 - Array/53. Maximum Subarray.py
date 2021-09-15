class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        
        maxEnd = nums[0]
        maxSoFar = nums[0]
        for i in range(1, len(nums)):
            maxEnd = maxEnd+nums[i]
            if maxEnd<nums[i]:
                maxEnd = nums[i]
            if maxSoFar<maxEnd:
                maxSoFar = maxEnd
        return maxSoFar
        