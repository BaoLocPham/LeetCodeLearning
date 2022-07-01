class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Sismilar to 3. Longest Substring Without Repeating Characters
        # instead of find maximumUniqueSubarray we find maximum sum of unique subarray
        # Time O(n)
        # Space O(n) store numSet
        if (len(nums)<=1):
            return sum(nums)
        l, maxSum = 0, 0
        numSet = set()
        curSum = 0
        for r in range(len(nums)):
            while (nums[r] in numSet):
                numSet.remove(nums[l])
                curSum -= nums[l]
                l +=1
            numSet.add(nums[r])
            curSum += nums[r]
            maxSum = max(maxSum, curSum)
        return maxSum