class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Approach Binary Search
        # Time O(logn)
        # Space O(1)
        def binarySearch(nums, target, leftBias):
            l, r = 0, len(nums)-1
            i  = -1
            while l<=r:
                mid = (l+r)//2
                val = nums[mid]
                if val<target:
                    l = mid + 1
                elif val>target:
                    r = mid - 1
                else:
                    i = mid
                    if leftBias: # if looking for the left most:
                        r = mid -1
                    else:
                        l = mid + 1
            return i
        leftMost = binarySearch(nums, target, True)
        rightMost = binarySearch(nums, target, False)
        return [leftMost, rightMost]