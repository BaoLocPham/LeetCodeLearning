class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #((2 ^ 2) ^ (1 ^ 1) ^ (4 ^ 4) ^ (5)) = > (0 ^ 0 ^ 0 ^ 5) = > 5.
        # Time O(n)
        # Space O(1)
        accumulate = 0
        for i in range(len(nums)):
            accumulate ^= nums[i]
        return accumulate