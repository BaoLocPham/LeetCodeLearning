class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1: counting
        # Time O(2n) -> requires 2 run, 1 for count, 1 for rewrite
        # Space O(1)
        # count0 = count1 = count2 = 0
        # for num in nums:
        #     if num == 0:
        #         count0 += 1
        #     elif num == 1:
        #         count1 += 1
        #     else:
        #         count2 += 1
        # for i in range(len(nums)):
        #     if count0:
        #         nums[i] = 0
        #         count0 -= 1
        #     elif count1:
        #         nums[i] = 1
        #         count1 -= 1
        #     else:
        #         nums[i] = 2

        # Approach 2: 3 pointers
        # Time O(n) -> 1 run
        # Space O(1)
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:  # nums[white]==2
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1