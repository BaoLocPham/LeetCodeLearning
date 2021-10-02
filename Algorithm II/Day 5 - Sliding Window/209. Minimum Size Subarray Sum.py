class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Approach 1: Sliding Window
        # Time O(n)
        # Space O(1)
        n = len(nums)
        left, minLength = 0, n + 1
        sumV = 0
        for right, val in enumerate(nums):
            sumV += val
            while sumV >= target:
                minLength = min(minLength, right - left + 1)
                sumV -= nums[left]
                left += 1
        # if the minLength is not changed then return 0 :)
        return minLength % (n + 1)