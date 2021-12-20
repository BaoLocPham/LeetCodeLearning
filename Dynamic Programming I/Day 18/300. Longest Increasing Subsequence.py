class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Approach 1: DP
        # Time O(n^2)
        # Space O(n)
        LIS = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j]>nums[i]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)
        # Approach 2: Patience Sorting
        # Time O(nlogn)
        # Space O(n)
        # https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf
        # in nutshell, the
        # tails[i] -> tail at piles i
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(size, i + 1)
        # size is the number of piles
        return size