class Solution:
    # Approach 1: Recursion + Top down
    # Time O(2^n) -> TLE of course :)
    # Space O(n)
    def rob(self, nums: List[int]) -> int:
        def rob(i):
            if i<0:
                return 0
            return max(rob(i-1), rob(i-2)+ nums[i])
        return rob(len(nums)-1)

    # Approach 2: Recursion + Top down + Memoi
    # Time O(n)
    # Space O(n)
    memoi = [-1] * (len(nums))
    def rob(i):
        if i < 0:
            return 0
        if memoi[i] >= 0:
            return memoi[i]
        memoi[i] = max(rob(i - 1), rob(i - 2) + nums[i])
        return memoi[i]
    return rob(len(nums) - 1)

    # Approach 3: Iterative + Memoi
    # Time O(n)
    # Space O(n)
    def rob(self, nums: List[int]) -> int:
        memoi = [0] * (len(nums) + 1)
        memoi[1] = nums[0]
        for i in range(1, len(nums)):
            memoi[i + 1] = max(memoi[i - 1] + nums[i], memoi[i])
        return memoi[len(nums)]

    # Approach 4: Iterative
    # Time O(n)
    # Space O(1)
    def rob(self, nums: List[int]) -> int:
        curr, prev = 0, 0
        for num in nums:
            tmp = curr
            curr = max(prev + num, curr)
            prev = tmp
        return curr