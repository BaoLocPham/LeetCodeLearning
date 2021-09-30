class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: Two pointers
        # Time O(logn + n) # sort the list and find two renain values
        # Space O(n)
        nums = sorted(nums)
        rs = []
        for i, num in enumerate(nums[:-1]):
            if i > 0 and num == nums[i-1]: # if there are target number already calculated, skip
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                summ = num + nums[l] + nums[r]
                if summ > 0:
                    r -= 1
                if summ < 0:
                    l += 1
                if summ == 0:
                    rs.append([num, nums[l], nums[r]])
                    # there are case of target number with multiple rs->we continue shift the left number
                    l += 1
                    while nums[l] == nums[l-1] and l<r :
                        l+=1
        return rs