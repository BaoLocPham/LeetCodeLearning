class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Time O(nlogn) # sort and traverse array once
        # Space O(1)
        nums.sort()
        median = nums[len(nums)//2]
        return sum(abs(n-median) for n in nums)