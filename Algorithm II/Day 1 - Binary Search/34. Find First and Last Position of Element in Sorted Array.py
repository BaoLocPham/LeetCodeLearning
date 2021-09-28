class Solution:
    # Approach 1: Binary Search
    # This problem is basically ask to find the first and the last position
    # Approach is binary search two times
    # one is find the left most aka the first
    # another is find the right most aka the last
    # Time O(logn)
    # Space O(1)
    def search(self, nums: List[int], target:int, isLeftBias:bool)->int:
        l, r = 0, len(nums)-1
        i=-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
            else:
                i = mid
                if isLeftBias:
                    r = mid-1
                else:
                    l = mid+1
        return i
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.search(nums, target, isLeftBias=True)
        right = self.search(nums, target, isLeftBias=False)
        return [left, right]