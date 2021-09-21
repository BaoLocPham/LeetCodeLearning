class Solution:
    # Approach 1: recursion
    # Time Limit Exceed :(
    # Time O(?) -
    # Because the same value in index i is process multiple times -> Need to optimized
    # Space O(?)
    """
    A robber has 2 options: a) rob current house i; b) don't rob current house.
    If an option "a" is selected it means she can't rob previous i-1 house but can safely proceed to the one before previous i-2 and gets all cumulative loot that follows.
    If an option "b" is selected the robber gets all the possible loot from robbery of i-1 and all the following buildings.
    So it boils down to calculating what is more profitable:

    robbery of current house + loot from houses before the previous
    loot from the previous house robbery and any loot captured before that
    rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )
    """
    # def robHouse(self, nums:List[int], i:int)->int:
    #     if i<0:
    #         return 0
    #     return max(self.robHouse(nums,i-2)+nums[i], self.robHouse(nums, i-1))
    # def rob(self, nums: List[int]) -> int:
    #     return self.robHouse(nums, len(nums)-1)

    # Approach 2: Optimize the approach 1
    # Time O(n) -> Only process the array once
    # Space O(n) -> size of the memo
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def robHouse(nums: List[int], i: int) -> int:
            if i < 0:
                return 0
            if memo[i] >= 0:
                return memo[i]
            rs = max(robHouse(nums, i - 2) + nums[i], robHouse(nums, i - 1))
            memo[i] = rs
            return rs
        return robHouse(nums, len(nums) - 1)

    # Approach 3: Get rid of the recursion
    # Time O(n)
    # Space O(n) -> size of the memo
    def rob(self, nums: List[int]) -> int:
        memo = [0] * (len(nums) + 1)
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            memo[i + 1] = max(memo[i - 1] + val, memo[i])
        return memo[len(nums)]

    # Approach 4: Use prev1, prev2
    # Because we only use the two latest variables
    # Time O(n)
    # Space O(1) -> two variable prev1,prev2 and tmp
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for num in nums:
            tmp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = tmp
        return prev1