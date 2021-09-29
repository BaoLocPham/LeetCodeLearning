class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Approach 1: Binary Search
        # Time O(logn)
        # Space O(1)
        l, r = 0, len(nums)-1
        minV = 5001
        while l<=r:
            mid = (l+r)//2
            minV = min(minV,  nums[mid])
            if nums[mid]<nums[r]:
                r = mid-1
            else: # nums[mid]>nums[r]
                l = mid+1
        return minV