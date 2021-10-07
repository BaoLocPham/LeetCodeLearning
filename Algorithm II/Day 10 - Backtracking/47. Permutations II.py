from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: Recursion backtracking
        # Time O(n*2^n)
        # Space O(n)
        rs = []
        # count = {n:0 for n in nums}
        # for num in nums:
        #     count[num]+=1
        count = Counter(nums)
        perm = []

        def dfs():
            if len(nums) == len(perm):
                rs.append(perm.copy())
                return
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    # recursion
                    dfs()
                    # backtracking
                    perm.pop()
                    count[n] += 1
        dfs()
        return rs