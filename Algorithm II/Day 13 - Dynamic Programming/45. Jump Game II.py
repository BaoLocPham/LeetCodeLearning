class Solution:
    def jump(self, nums: List[int]) -> int:
        # Approach 1: Greedy ~ BFS look like
        # Time O(n)
        # Space O(1)
        rs = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            # update window: l and r
            l = r + 1 # adjacent to r
            r = farthest # farthest the current window can reach
            rs += 1  # count minimum of jumps
        return rs
