class Solution:
    def rob(self, nums: List[int]) -> int:
        # Approach 1: Dynamic Programming:
        # This problem is basically ask you to run 2 sub house robber I on the list
        # 1 -> exclude the last house
        # 2 -> exclude the first house
        # Time O(n)
        # Space O(1)
        def robHelper(houses):
            prev2, prev1 = 0, 0
            for num in houses:
                tmp = prev1
                prev1 = max(prev2+num, prev1)
                prev2 = tmp
            return prev1
        rs = max(nums[0], robHelper(nums[:-1]), robHelper(nums[1:]))
        return rs