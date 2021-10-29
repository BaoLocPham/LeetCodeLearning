class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Approach 1: Two pointers?
        # Time O(n)
        # Space O(1)
        # start with two largest values, as soon as we find a number bigger than both, while both have been updated, return true.
        first, second = float('inf'), float('inf')
        for num in nums:
            if num<=first:
                first = num
            elif num<=second:
                second = num
            else: # find the third number larger than the first and the second
                return True
        return False