class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # Approach 1: DP
        # Time O(n^2)
        # Space O(n)
        n = len(nums)
        LIS = [0] * n  # longest increasing subsequence ending at i
        count = [0] * n  # number of ways to form LIS ending at i

        ans, maxLen = 0, 0

        for i in range(n):
            curr = nums[i]
            total = 0
            l = 1
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                if LIS[j] + 1 == l:
                    total += count[j]
                elif LIS[j] + 1 > l:
                    l = LIS[j] + 1
                    total = count[j]
            LIS[i] = l
            count[i] = max(1, total)
            if l > maxLen:
                maxLen = l
                ans = count[i]
            elif l == maxLen:
                ans += count[i]
        return ans

