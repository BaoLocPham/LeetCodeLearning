class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach 1:
        # Using set or hashMap to store the number
        # Time O(n)
        # Space O(n) size of the set, hashMap
        # sett = set()
        # for i, num in enumerate(nums):
        #     if num in sett:
        #         sett.remove(num)
        #     else:
        #         sett.add(num)
        # return sett.pop()
        
        # Approach 2: using XOR operator
        # Concept: a^b=b^a
        # a^b^b = b^a^a = a-> a is appear once
        # Time O(n)
        # Space O(1)
        accumulate = 0
        for i in range(len(nums)):
            accumulate ^= nums[i]
        return accumulate