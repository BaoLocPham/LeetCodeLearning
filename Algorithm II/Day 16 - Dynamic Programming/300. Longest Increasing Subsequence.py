class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Approach 1: DP
        # Time O(n^2)
        # Space O(n) 
        LST = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    LST[i] = max(LST[i], 1 + LST[j])
        return max(LST)