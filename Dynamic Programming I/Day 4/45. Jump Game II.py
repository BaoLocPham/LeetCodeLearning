class Solution:
    def jump(self, nums: List[int]) -> int:
        # Approach 1: BFS
        # Time O(n)
        # Space O(1)
        rs, l, r = 0, 0, 0
        goal = len(nums)-1
        while r<goal:
            furthest = 0
            for i in range(l, r+1):
                furthest = max(furthest, i+nums[i])
            # update pointer
            l +=1
            r = furthest
            rs+=1
        return rs