class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: two pointers
        # Time O(nlogn + n)
        # Space O(n)
        nums = sorted(nums)
        rs = []
        for i, num in enumerate(nums[:-1]):
            if i>0 and num==nums[i-1]: # if number is already calculated
                continue # skip the number
            l = i+1
            r = len(nums)-1
            while l<r:
                sumV = num+nums[l]+nums[r]
                if sumV<0:
                    l+=1
                elif sumV>0:
                    r-=1
                else: # sumV == 0 -> found a triple
                    rs.append([num, nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return rs