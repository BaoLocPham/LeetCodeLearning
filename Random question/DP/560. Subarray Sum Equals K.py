class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Time O(n)
        # Space O(n)
        ans = 0
        prefsum = 0
        d = {0:1}
        for num in nums:
            prefsum += num
            if prefsum-k in d:
                ans += d[prefsum-k]
            if prefsum in d:
                d[prefsum] +=1
            else:
                d[prefsum] = 1
        return ans