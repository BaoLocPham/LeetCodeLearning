class Solution:
    """
    We need to make prefix_sum + suffix_sum = x. 
    But instead of this, finding a subarray whose sum is sum(nums) - x will do the job. 
    Now we only need to maximize the length of this subarray to minimize 
    the length of prefix + suffix, which can be done greedily. 
    By doing this, we can get the minimum length, i.e., 
    the minimum number of operations to reduce x to exactly 0 (if possible).
    OG: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/2136555/C%2B%2BPython-Simple-Solution-w-Explanation-or-Sliding-Window
    """
    def minOperations(self, nums: List[int], x: int) -> int:
        # Sliding window
        # Time O(n) # the startIndx and endIndx only travels through the array once.
        # Space O(1)
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        currSum, maxLen = 0, 0
        startIndx = 0
        for endIndx in range(len(nums)):
            currSum += nums[endIndx]
            while startIndx <= endIndx and currSum>target:
                currSum -= nums[startIndx]
                startIndx += 1
            if currSum==target:
                maxLen = max(maxLen, endIndx-startIndx+1)
        return len(nums) - maxLen if maxLen else -1