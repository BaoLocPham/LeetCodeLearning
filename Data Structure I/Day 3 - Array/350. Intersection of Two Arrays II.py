class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Approach 1: using hashMap
        # Time o(?)
        # Space O(n) size of hashMap
        # table = {}
        # rs = []
        # for num in nums1:
        #     if num not in table:
        #         table[num] = 0
        #     table[num] +=1
        # for num in nums2:
        #     if num in table and table[num]>0:
        #         rs.append(num)
        #         table[num] -=1
        # return rs

        # Approach 2: Two pointers
        # Time O(n)
        # Space O(n) size of temp array
        l = r = 0
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        rs = []
        while (r<len(nums1) and l<len(nums2)):
            if nums1[r] == nums2[l]:
                rs.append(nums1[r])
                l+=1
                r+=1
            elif nums1[r]<nums2[l]:
                r+=1
            else: # nums1[r]>nums2[l]
                l+=1
        return rs