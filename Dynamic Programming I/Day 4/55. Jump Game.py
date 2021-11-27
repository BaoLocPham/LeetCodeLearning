class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Approach 1: Going forward
        # Time O(n)
        # Space O(1)
        end = 0
        for i, n in enumerate(nums):
            if i>end: # that's mean at the previous step
                # we cann't not reach the last end
                return False
            # new end
            # if i+n cannot reach current end
            # then after next loop will be False
            end = max(end, i+n)
        return True

        # Approach 2: Going backward
        # Time O(n)
        # Space O(1)
        goal = len(nums)-1
        for i in range(len(nums))[::-1]:
            if i+nums[i]>=goal:
                goal = i
        return not goal

        # Approach 3: one-liner very pythonic 
        # Time O(n)
        # Space O(1)
        # tup = (i, n)
        # when reduce have the 3rd parameter-> will passed as the first argument in the lambda function
        # Although Guido van Rossum hate reduce but it's still very efficient for show off your coding skill ¯\_(ツ)_/¯
        return reduce(lambda end, tup: max(end, tup[0] + tup[1]) * (tup[0] <= end), enumerate(nums, 1), 1) > 0