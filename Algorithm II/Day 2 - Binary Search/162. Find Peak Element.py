class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Approach 1: Linear search
        # Time O(n)
        # Space O(1)
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return i
        return len(nums)-1
        # Approach 2: Binary Search
        # Time O(logn)
        # Space O(1)
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[mid+1]:
                r = mid
            else: # nums[mid]<nums[mid+1]
                l = mid+1
        return l