class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums = map(lambda x: x**2, nums)
        # return sorted(nums)
        
        ## O(n) -> 
        n = len(nums)
        mid = 0
        for mid in range(n):
            if (nums[mid]>=0):
                break
        # Split the array to the positive and negative part
        left = mid-1 # first half
        right = mid # second half
        indx = 0
        rs = [0]*n
        while left>=0 and right<n:
            if nums[left]**2>nums[right]**2:
                rs[indx] = nums[right]**2
                right+=1
            else:
                rs[indx] = nums[left]**2
                left-=1
            indx+=1
        while(left>=0):
            rs[indx] = nums[left]**2
            left-=1
            indx+=1
        while(right<n):
            rs[indx] = nums[right]**2
            right +=1
            indx +=1
        return rs