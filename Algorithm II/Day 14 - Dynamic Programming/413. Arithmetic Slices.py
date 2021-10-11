class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Approach 1: DP
        # Time O(n)
        # Space O(n)
        n = len(nums)
        dp = [0]*n
        ans = 0
        for i in range(2, n):
            if nums[i-1]-nums[i-2]==nums[i]-nums[i-1]:
                dp[i] = dp[i-1]+1
            ans += dp[i]
        return ans

        # Approach 2: DP optimized memory
        # Time O(n)
        # Space O(1)
        n = len(nums)
        dp, dpPrev = 0, 0
        ans = 0
        for i in range(2, n):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                dp = dpPrev + 1
            ans += dp
            dpPrev = dp
            dp = 0
        return ans