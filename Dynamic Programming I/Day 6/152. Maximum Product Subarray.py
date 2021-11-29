class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Approach 1: Brute force, TLE :))
        # Time O(n^2)
        # Space O(1)
        rs = nums[0]
        n = len(nums)
        for i in range(n):
            mul = nums[i]
            for j in range(i+1, n):
                rs = max(rs, mul)
                mul *= nums[j]
            rs = max(rs, mul)
        return rs

        # Approach 2: DP
        # keep track of maxV and minV when travel the array
        # Time O(n)
        # Space O(1)
        rs = nums[0]
        minV = maxV = 0
        for i in range(len(nums)):
            tmp1 = maxV*nums[i]
            tmp2 = minV*nums[i]
            maxV = max(tmp1, tmp2, nums[i])
            minV = min(tmp1, tmp2, nums[i])
            rs = max(rs, maxV)
        return rs

        # Approach 3: Prefix, Suffix
        # Time O(n)
        # Space O(n)
        A = nums
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)