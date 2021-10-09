class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Approach 1: Greedy approach
        # Time O(n)
        # Loop start from the end of the list
        # shift the goal if that index+max_val_jump can reach the goal
        # Space O(1)
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                # shift the goal to the left
                goal = i
        return True if goal == 0 else False
