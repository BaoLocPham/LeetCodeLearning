class Solution(object):
    def combinationSum4(self, nums, target):
        # Approach 1: DP
        # TIme O(n*m)
        # Space O(n+m)
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]