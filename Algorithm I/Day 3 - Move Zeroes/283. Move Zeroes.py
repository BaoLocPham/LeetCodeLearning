class Solution:
    def moveZeroes_1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # this answer is Time: O(n) using additional array
        # space O(n)
        rs = []
        i =0
        for n in nums:
            if n==0:
                i+=1
        j= 0
        while j<len(nums):
            if nums[j]!=0:
                rs.append(nums[j])
            j+=1
        while(i>0):
            rs.append(0)
            i-=1
        for i, n in enumerate(rs):
            nums[i] = n
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # This approach using two pointers
        # One iterate over the array
        # One is keep track of the lastNoneZeroIndex
        lastNoneZeroIndex = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[lastNoneZeroIndex] = nums[i]
                lastNoneZeroIndex+=1
        for i in range(lastNoneZeroIndex, len(nums)):
            nums[i] = 0