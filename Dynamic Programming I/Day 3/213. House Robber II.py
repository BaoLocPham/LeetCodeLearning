class Solution:
    # Approach 1: DP
    # Nothing fancy here, just run two sub house robber I
    # Time O(n)
    # Space O(1)
    def rob(self, nums: List[int]) -> int:
        def house_robberI(house):
            prev1, prev2 = 0, 0
            for num in house:
                tmp = prev1
                prev1 = max(prev2+num, prev1)
                prev2 = tmp
            return prev1
        rs = max(nums[0], house_robberI(nums[:-1]), house_robberI(nums[1:]))
        return rs