class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Approach 1: Binary search
        # Concept is explained in the whiteboard
        # Time O(logn)
        # Space O(1)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:  # t<mid and t>l
                    r = mid - 1
            else:  # nums[l]>nums[mid]
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:  # t>mid and t<r
                    l = mid + 1
        return -1
