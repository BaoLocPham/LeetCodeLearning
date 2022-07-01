class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # Approach: Greedy
        # Time O(n)
        # Space O(1)
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1]>nums[i]:
                count+=1
                if (i-2<0 or nums[i-2]<=nums[i]):
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return count<=1