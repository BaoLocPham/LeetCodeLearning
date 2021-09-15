class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        rs = nums.copy()
        for i in range(n):
            final_pos = (i+k)%n
            nums[final_pos] = rs[i]